import os
import json
from consts import ROOT_PATH

class FileHandler:
    def __init__(self):
        pass

    def _has_file(self):
        files = os.listdir(ROOT_PATH)

        return bool(files)
    
    def _create_file(self):
        with open(f"{ROOT_PATH}/task-tracker.json", "x") as f:
            d = {"id": 3423, "desc": "helloooo"}
            f.write(json.dumps(d))
    
    def fsdf(self):
        if self._has_file():
            print("Tracker уже создан ;)")
        else:
            print("Tracker еще не создан ;(")
            self._create_file()
    
    