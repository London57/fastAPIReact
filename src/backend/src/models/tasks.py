from sqlalchemy.orm import Mapped

from src.db.db import Base
from src.schemas.tasks import TaskSchema

print('v task')
class Task(Base):
    __tablename__ = "tasks"
    title: Mapped[str]
    employeer_id: Mapped[int]
    employee_id: Mapped[int]
    
    def to_read_model(self) -> TaskSchema:
        return TaskSchema(
					id = self.id,
					title = self.title,
					employee_id = self.employee_id,
          employeer_id = self.employeer_id,
        )
