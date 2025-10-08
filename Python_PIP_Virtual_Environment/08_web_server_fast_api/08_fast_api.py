'''

univcorn: 
- Asynchronous Server Gateway Interface 
- Web server for Python web apps

execute: 
uvicorn file_name:app --reload

:app = the name of the app variable that contains the FastAPI() module.

''' 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
  return [
    1,2,3
  ]

@app.get('/contact')
def get_contact():
  return {
    'name': 'Test'
  }

@app.get("/items", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

def run():
  pass

if __name__ == '__main__':
  run()