from datetime import datetime

class Task:
    def __init__(self, id, description: str | None = None):
        self.id = id
        self.description = description
        self.status = "pending"
        self.createdAt = datetime.now()
        self.updatedAt = self.createdAt

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat(),
        }
