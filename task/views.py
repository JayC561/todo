from django.shortcuts import render
from django.views.generic import View
from .models import Task as Task_db
import json
from django.http import HttpResponse
from .mixins import TaskSerializeMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .utils import is_json, get_object_by_id
from .forms import TaskForm

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')   # class crsf_exempt
class Task(View, TaskSerializeMixin):
    def get(self, request, id, *args, **kwargs):
        try:
            query = Task_db.objects.get(id = id)
        except Task_db.DoesNotExist:
            json_data = json.dumps({'msg':'Invalid ID'})
            return HttpResponse(json_data, content_type='application/json', status=404)
        else:
            json_data = self.serialize([query,])
            return HttpResponse(json_data, content_type='application/json', status=200)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Invalid JSON data'})
            return HttpResponse(json_data, content_type='application/json', status=400)
        task = json.loads(data)
        form = TaskForm(task)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Saved Successfully'})
            return HttpResponse(json_data, content_type='application/json', status=200)
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json', status=400)

    def put(self, request, id, *args, **kwargs):
        task = get_object_by_id(id)
        if task is None:
            json_data = json.dumps({'msg': 'Invalid ID'})
            return HttpResponse(json_data, content_type='application/json', status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Invalid JSON data'})
            return HttpResponse(json_data, content_type='application/json', status=400)
        task_updates = json.loads(data)
        task_data = {
            'title': task.title,
            'check': task.check,
            'date_to_do': task.date_to_do
        }
        task_data.update(task_updates)
        form = TaskForm(task_data, instance=task)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Saved Successfully'})
            return HttpResponse(json_data, content_type='application/json', status=200)
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json', status=400)

    def delete(self, request, id , *args, **kwargs):
        task = get_object_by_id(id)
        if task is None:
            json_data = json.dumps({'msg': 'Invalid ID'})
            return HttpResponse(json_data, content_type='application/json', status=404)
        t = task.delete()
        print(t)
        json_data = json.dumps({'msg': 'Deleted Successfully'})
        return HttpResponse(json_data, content_type='application/json', status=200)


class TaskList(View, TaskSerializeMixin):
    def get(self, request, *args, **kwargs):
        query = Task_db.objects.all()
        json_data = self.serialize(query)
        return HttpResponse(json_data, content_type='application/json')
