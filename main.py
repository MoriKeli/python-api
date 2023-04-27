from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    data = {
        "name": "Mori Keli",
    }
    return data

students = {
    1: {
        "name": "student",
        "age": 20,
        "campus": "campo 1",
    }
}

# url python
@app.get("/students/{student}")
def get_student(student: int = Path(description='Enter student ID', gt=0, lt=3)):
    return students[student]

# Querying data
@app.get('/student/name')
def get_student_info(name: Optional[str]):
    for obj in students:
        if students[obj]["name"] == name:
            return students[obj]

    return {'data': 'Data does not exist!'}

@app.get('/student/{student_id}')
def get_student_info(student_id: int, name: Optional[str]):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {'data': 'Data does not exist!'}


class Student(BaseModel):
    name: str
    age: int
    campus: str

class UpdateStudentInfo(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    campus: Optional[str] = None


# POST method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"ERROR": "Student exists!"}

    students[student_id] = student
    return students[student_id]


# PUT method
@app.put('/update/student/{student_id}')
def update_student(student_id: int, student: UpdateStudentInfo):
    if student_id not in students:
        return {"ERROR": "Student does not exist!"}

    if student.name is not None:
        students[student_id].name = student.name

    if student.age is not None:
        students[student_id].age = student.age

    if student.campus is not None:
        students[student_id].campus = student.campus

    return students[student_id]

# DELETE method
@app.delete('/delete/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {"ERROR": "Student does not exist!"}

    del students[student_id]
    return {"message": "Student successfully deleted!"}

