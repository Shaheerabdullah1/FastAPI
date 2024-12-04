from fastapi import FastAPI


#created the instance
app = FastAPI()

#how to start the server
@app.get('/')
def index():
    return {'data' : {'name':'Shaheer'}}

#how to start the server with custom route
@app.get('/about')
def about():
    return {'data' : 'about-page'}

