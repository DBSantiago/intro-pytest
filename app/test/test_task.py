from datetime import datetime, timedelta
import pytest

from app.task import Task, DueDateError

# Las funciones fixture tienen como objetivo pasar valores como parámetro a nuestras pruebas
# Y deben llamarse igual que dicho parámetro


@pytest.fixture
def username():
    return "dbsantiago"


@pytest.fixture
def password():
    return "12345"


def test_username(username):
    assert username == "dbsantiago"


def test_username_and_password_(username, password):
    assert username == "dbsantiago"
    assert password == "12345"


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

    @pytest.mark.skip(reason="This test is skipped because we say so.")
    def test_skip(self):
        pass

    @pytest.mark.skipif(True, reason="This test is skipped because passed condition is True.")
    def test_skipif(self):
        pass
