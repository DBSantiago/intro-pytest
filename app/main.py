from datetime import datetime
from datetime import timedelta

from app.task import Task


def main():
    task = Task("Title", "Description", "User", datetime.now())
    # task2 = task = Task("Title", "Description", "User", datetime.now() - timedelta(days=1))


if __name__ == "__main__":
    main()
