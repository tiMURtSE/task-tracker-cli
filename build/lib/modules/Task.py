from datetime import datetime

class Task:
    def __init__(self, id, description: str):
        self.id = id
        self.description = description
        self.status = "todo"
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }