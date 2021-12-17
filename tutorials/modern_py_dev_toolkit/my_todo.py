"""Main module."""

# Show a list of tasks
# Add a new task
# Mark task as complete
# Delete a task w/o marking it as done

class Task():
    def __init__(self, description) -> None:
        self.description = description
        self.status = False

    def __str__(self):
        check = " X"[self.status]
        return f"[{check}]{' '*3}{self.description}"
    
    def update_status(self):
        if self.status:
            self.status = False
        else:
            self.status = True

class ToDo():
    def __init__(self, name) -> None:
        self.name = name
        self.tasks = []
    
    def __str__(self):
        s = ''
        s += f"{self.name}\n"
        for _ in enumerate(self.tasks, start=1):
            n, task = _
            s += f"{n}\t{task}\n"
        return s    

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task(self, selection):
        offset = selection - 1
        self.tasks[offset].update_status()
    
    def del_task(self, selection):
        offset = selection - 1
        del self.tasks[offset]
        

if __name__ == "__main__":
    eg = Task("fold laundry and iron shirts")
    print(eg)
    my_todo = ToDo("URGENT")
    my_todo.add_task("make a todo list")
    my_todo.add_task("eat some pizza")
    print(my_todo)
    my_todo.mark_task(2)
    print(my_todo)
    my_todo.del_task(1)
    print(my_todo)