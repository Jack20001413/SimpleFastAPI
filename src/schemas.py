from pydantic import BaseModel


class StudentModel(BaseModel):
    first_name: str
    last_name: str