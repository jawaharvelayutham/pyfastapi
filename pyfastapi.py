# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'hi  ': 'this is jawahar'}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
