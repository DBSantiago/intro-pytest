from datetime import datetime
import pytest

from app.task import Task


class TestTask:

    def test_task(self):
        assert True

    def test_new_task(self):
        date = datetime.now()
        task = Task("Test this", "Testing new task", "dbsantiago", date)

        assert task.title == "Test this"
        assert task.description == "Testing new task"
        assert task.assigned_to == "dbsantiago"
        assert task.due_date == date
