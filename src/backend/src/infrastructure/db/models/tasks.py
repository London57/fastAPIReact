from sqlalchemy.orm import Mapped

from src.infrastructure.db.models import Base
from src.domain.schemas.tasks import TaskSchema

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
