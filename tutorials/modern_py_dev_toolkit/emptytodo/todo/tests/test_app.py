from todo.api import create_task, delete_task, get_tasks, finish_task, delete_task


def test_list_tasks(test_app):
    assert get_tasks() == []
    create_task("make a cake")
    create_task("make a cake")
    assert len(get_tasks()) == 2

def test_create_task(test_app):
    create_task("milk a cow")
    existing_tasks = get_tasks()
    assert len(existing_tasks) == 1
    first_task = existing_tasks[0]
    assert first_task.body == "milk a cow"
    assert first_task.done is False

def test_finish_task(test_app):
    create_task("borrow eggs from a hen")
    assert len(get_tasks()) == 1
    
    get_eggs = get_tasks().pop()
    get_eggs_id = get_eggs.id
    finish_task(get_eggs_id)
    
    get_eggs = get_tasks().pop()
    assert get_eggs.done is True

def test_delete_task(test_app):
    create_task("borrow eggs from a hen")
    assert len(get_tasks()) == 1
    
    get_eggs = get_tasks().pop()
    get_eggs_id = get_eggs.id
    delete_task(get_eggs_id)
    
    assert len(get_tasks()) == 0
