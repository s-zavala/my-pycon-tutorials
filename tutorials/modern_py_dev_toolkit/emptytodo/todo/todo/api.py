"""API functions to interact with TODO tasks."""
from todo.models import Task, db


def create_task(body):
    """Create a new task in DB.
    
    :param body: Text of a Todo task
    :type body: str
    """
    task = Task(body=body)
    db.session.add(task)
    db.session.commit()


def get_tasks():
    return Task.query.all()

def finish_task(task_id):
    """Mark task as done.

    :param task_id: ID of the task to finish
    :type task_id: int
    """
    task = Task.query.get(task_id)
    task.done = True
    db.session.commit()

def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
