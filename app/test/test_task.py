from datetime import datetime, timedelta
import pytest

from app.task import Task, DueDateError


class TestTask:

    def test_task(self):
        assert True

    def test_new_task(self):
        date = datetime.now() + timedelta(days=1)
        task = Task("Test this", "Testing new task", "dbsantiago", date)

        assert task.title == "Test this"
        assert task.description == "Testing new task"
        assert task.assigned_to == "dbsantiago"
        assert task.due_date == date

    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            date = datetime.now() - timedelta(days=1)
            task = Task("Test this", "Testing new task", "dbsantiago", date)
