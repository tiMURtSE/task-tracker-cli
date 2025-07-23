import os
import json
from modules.Task import Task
from consts import ROOT_PATH

class FileHandler:
    '''Работает с изменениями в файле'''
    def __init__(self):
        self._is_file_created = self.has_file()
        self._create_file()

    def _create_file(self):
        if not self._is_file_created:
            with open(f"{ROOT_PATH}/task-tracker.json", "x") as f:
                storage = {"tasks": []}
                f.write(json.dumps(storage))
            
            self._is_file_created = True

    def _get_tasks(self):
        storage = None

        with open(f"{ROOT_PATH}/task-tracker.json", "r") as f:
            storage = json.loads(f.read())["tasks"]

        return storage
    
    def _update_tasks(self, tasks):
        with open(f"{ROOT_PATH}/task-tracker.json", "w") as f:
            storage = {"tasks": tasks}
            f.write(json.dumps(storage))
    
    def has_file(self):
        files = os.listdir(ROOT_PATH)

        return bool(files)
    
    def add_new_task(self):
        tasks = self._get_tasks()

        new_id = self._get_new_task_id(tasks)
        new_task = Task(new_id).to_dict()
        tasks.append(new_task)

        self._update_tasks(tasks=tasks)

    def _get_new_task_id(self, tasks):
        id = 1

        if tasks:
            latest_task = max(tasks, key=lambda task: task["id"])
            id = latest_task["id"] + 1

        return id
    
    # def init_tracker(self):
    #     '''Если файл трекера еще не создан, то создает его'''
    #     if self._has_file():
    #         print("Tracker уже создан ;)")
    #     else:
    #         print("Tracker еще не создан ;(")