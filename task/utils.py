import json
from .models import Task as Task_db


def is_json(data):
    try:
        data = json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid


def get_object_by_id(task_id):
    try:
        task = Task_db.objects.get(id=task_id)
    except Task_db.DoesNotExist:
        task = None
    return task
