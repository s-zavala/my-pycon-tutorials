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

if __name__ == "__main__":
    eg = Task("fold laundry and iron shirts")
    print(eg)