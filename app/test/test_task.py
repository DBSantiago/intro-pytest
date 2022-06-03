from datetime import datetime, timedelta
import pytest

from app.task import Task, DueDateError


class TestTask:

    @pytest.mark.news
    def test_task(self):
        assert True

    @pytest.mark.news
    def test_new_task(self):
        date = datetime.now() + timedelta(days=1)
        task = Task("Test this", "Testing new task", "dbsantiago", date)

        assert task.title == "Test this"
        assert task.description == "Testing new task"
        assert task.assigned_to == "dbsantiago"
        assert task.due_date == date

    @pytest.mark.due_date
    @pytest.mark.errors
    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            date = datetime.now() - timedelta(days=1)
            task = Task("Test this", "Testing new task", "dbsantiago", date)

    @pytest.mark.due_date
    def test_due_date(self):
        date = datetime.now() + timedelta(days=1)
        task = Task("Test this", "Testing new task", "dbsantiago", date)

        assert date > datetime.now()
