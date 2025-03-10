from pydantic import BaseModel
from typing import List

class GenerateTaskRequest(BaseModel):
    preferences: List[str]