from fastapi import FastAPI

app = FastAPI()

#my_first_api = FastAPI()
# path
#POST, PUT, DELETE, GET
'''
POST - To create the Data
PUT - To Update the Data
GET - To Read the Data
DELETE - To Delete the Data
'''

'''
@ path operation decorator, Syntax in python we call this as decorator. Takes the function below and does something with it
The function below corresponds with the path of root and perform get 
get is the http get operation
("/") the path here it is root
'''
@app.get("/")
#@my_first_api.get("/")
async def root():
    return {"message": "Hello World from FASTAPI"}

# @app.put()
# @app.post()
# @app.delete()

# async def root() is a pyhton function
# async function we can also write normal function
# return python dictionary, string, int, list etc

@app.get("/demo")
def demo_func():
    return {"message":"Output from demo function"}
# write at the end of url /demo to see only demo function output

@app.post("/post_demo")
def demo_post():
    return {"message":"Output from post demo function"}