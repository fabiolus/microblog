#All routes will be listed here
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

