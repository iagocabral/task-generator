from pydantic import BaseModel

class TaskBase(BaseModel):
    description: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True