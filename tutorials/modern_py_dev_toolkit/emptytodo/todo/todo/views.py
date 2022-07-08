"""URLs for our application."""

from flask import render_template, request, redirect
from todo import app
from todo.api import create_task, delete_task, get_tasks, finish_task, delete_task

# TODO: Write URLs for the application
@app.route("/")
def tasks_list():
    tasks = get_tasks()
    # Render the HTML page located in "templates/application.html"
    # Passing tasks as a variable, so it can be used in the template
    return render_template("application.html", tasks=tasks)

@app.route("/task", methods=["POST"])
def task_create():
    body = request.form["body"]
    create_task(body)
    return redirect("/")

@app.route("/done/<int:task_id>")
def task_done(task_id):
    finish_task(task_id)
    return redirect("/")

@app.route("/delete/<int:task_id>")
def task_delete(task_id):
    delete_task(task_id)
    return redirect("/")
