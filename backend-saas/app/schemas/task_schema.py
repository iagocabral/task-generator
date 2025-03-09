from pydantic import BaseModel, ConfigDict

class TaskBase(BaseModel):
    description: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)