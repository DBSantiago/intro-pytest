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
    @pytest.mark.parametrize(
        "title, description, assigned_to, due_date",
        [
            ("Title 1", "Description 1", "User 1", datetime.now() + timedelta(days=1)),
            ("Title 2", "Description 2", "User 2", datetime.now() + timedelta(days=1)),
            ("Title 3", "Description 3", "User 3", datetime.now() + timedelta(days=1)),
            ("Title 4", "Description 4", "User 4", datetime.now() + timedelta(days=1)),
        ]
    )
    def test_new_task(self, title, description, assigned_to, due_date):
        date = datetime.now() + timedelta(days=1)
        task = Task(title, description, assigned_to, date)

        assert task.title == title
        assert task.description == description
        assert task.assigned_to == assigned_to
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
