import os
import json
from datetime import datetime
from modules.Task import Task
from consts import ROOT_PATH

class Storage:
    '''Работает с изменениями в файле'''
    def __init__(self):
        self._is_file_created = self.has_file()
        self._create_file()

    def _create_file(self):
        '''Создает пустой json-файл.'''
        if not self._is_file_created:
            with open(f"{ROOT_PATH}/task-tracker.json", "x") as f:
                storage = {"tasks": []}
                f.write(json.dumps(storage))
            
            self._is_file_created = True

    def _get_tasks(self):
        '''Получает все задачи в виде списка.'''
        storage = None

        with open(f"{ROOT_PATH}/task-tracker.json", "r") as f:
            storage = json.loads(f.read())["tasks"]

        return storage
    
    def _update_tasks(self, tasks):
        with open(f"{ROOT_PATH}/task-tracker.json", "w") as f:
            storage = {"tasks": tasks}
            f.write(json.dumps(storage))

    def _get_new_task_id(self, tasks):
        id = 1

        if tasks:
            latest_task = max(tasks, key=lambda task: task["id"])
            id = latest_task["id"] + 1

        return id
    
    def _print_tasks(self, tasks):
        ''' #1: task: "desc" status: "" дата создания: "createdAt"'''

        for task in tasks:
            print(f"#{task["id"]} task: {task["description"]} status: {task["status"]}")
    
    def has_file(self):
        files = os.listdir(ROOT_PATH)

        return bool(files)
    
    def add_new_task(self, description: str):
        tasks = self._get_tasks()

        new_id = self._get_new_task_id(tasks)
        new_task = Task(new_id, description).to_dict()
        tasks.append(new_task)

        self._update_tasks(tasks=tasks)

    def delete_task(self, id: int):
        tasks = self._get_tasks()

        filtered_tasks = [task for task in tasks if task["id"] != id]

        self._update_tasks(tasks=filtered_tasks)

    def list_tasks(self, status: str = None):
        tasks = self._get_tasks()
        filtered_tasks = []

        match status:
            case "todo":
                filtered_tasks = [task for task in tasks if task["status"] == "todo"]
            case "in-progress":
                filtered_tasks = [task for task in tasks if task["status"] == "in-progress"]
            case "done":
                filtered_tasks = [task for task in tasks if task["status"] == "done"]
            case _:
                self._print_tasks(tasks)
                
        self._print_tasks(filtered_tasks)

    def update_tasks(self, id: int, description: str):
        tasks = self._get_tasks()

        for task in tasks:
            if int(task["id"]) == id:
                task["description"] = description
                task["updated_at"] = datetime.now().isoformat()

        self._update_tasks(tasks)