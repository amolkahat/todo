from django.test import TestCase, Client

from app_todo.models import tasks
# Create your tests here.
from datetime import datetime

class ModelTests(TestCase):

    def setUp(self):
        time = datetime.now()
        todo = tasks.objects.create(task_text='Todo', completed_date=time, added_date=time,state=-1)
        done = tasks.objects.create(task_text='Done', completed_date=time, added_date=time,state=-1)

    def test_models_db_using_id(self):
        todo = tasks.objects.get(id=1)
        done = tasks.objects.get(id=2)
        assert 'Todo' in todo.task_text
        assert 'Done' in done.task_text

    def test_gui(self):
        c = Client()
        response = c.post('/todo/', {'task_text':'Python'})
        assert response.status_code == 200
