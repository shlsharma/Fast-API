from pydantic import BaseModel

data = {
    "name": "Sahil",
    "age": "28",
    "course": "MLOps Bootcamp",
    "ratings": [4, 4, "4", "5", 4]
}

class Instructor(BaseModel):
    name: str
    age: int
    course: str
    ratings: list[int] = []

user = Instructor(**data)

print(f'Found a Instructor: {user}')