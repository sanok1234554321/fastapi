from typing import List,Optional
from urllib import response
from fastapi import Response
from fastapi.responses import HTMLResponse 
from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def main():
    return {"message": "hello world"}

@app.get("/user/{userID}")
async def notmain(userID):
    return {"ID": userID}

@app.get("/mol")
async def copyofmain():
    return HTMLResponse("<h1>Hi There</h1>")

@app.get("/lom")
async def copyofcopy(response: Response):
    response.headers["new_header"] = "crowbar"
    return {"message": "мы поменяли загаловок!"}

@app.get("/molotok")
async def copyofcopyofcopy(response: Response):
    response.set_cookie(key="nothing",value="nothingtoo")
    return {"message": "мы поменяли Cookie!"}

    