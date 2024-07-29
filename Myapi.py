from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import json
import os

app = FastAPI()

students = {
    1: {
        "name":"tanay",
        "age" :"20",
        "class":"TY"
    },
     2: {
        "name": "pranav",
        "age": "21",
        "class": "TY"
    },
    3: {
        "name": "aryan",
        "age": "20",
        "class": "TY"
    }
} 


class Student(BaseModel):
    name : str
    age: int
    year: str

class updatestudent(BaseModel):
    name: Optional[str]= None
    age: Optional[int]= None
    year:Optional[str]= None    


@app.get("/")
def index():
    return {"name": "First data"} 

@app.get("/get_student/{student_id}")
def get_student(student_id: int = Path(description="The ID of student you want to view", gt=0, lt=5)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(student_id: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return{"data": "not found"} 

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return{"student alrady exists"}
    students[student_id]= student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: updatestudent):
    if student_id not in students:
        return{"student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]    

def get_dataframe_from_json(filepath: str = "home/tanay/Documents/fastapi/Myapi.py") -> pd.DataFrame:
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file at path {filepath} was not found.")
    with open(filepath, 'r') as file:
        data = json.load(file)
    return pd.DataFrame(data)

@app.get("/questions")
def load_questions():
    df = get_dataframe_from_json()
    return df.to_string()

@app.get("/questions-json")
def load_questions_json():
    df = get_dataframe_from_json()
    return df.to_json(orient="records")