from datetime import datetime
import logging
# LOGGING_TYPE=PRIORITY_LEVEL
# DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50
logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)s - %(asctime)s - Message: %(message)s",
                    filename="logging_task.log",
                    filemode="a"
                    )


class DueDateError(Exception):
    pass


class Task:

    def __init__(self, title, description, assigned_to, due_date):
        logging.debug("Checking if due_date is valid...")
        if due_date < datetime.now():
            logging.error("Due date can't be in the past.")
            raise DueDateError

        logging.info("Creating new task object.")
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.due_date = due_date
