from fastapi import FastAPI


#created the instance
myapp = FastAPI()

#how to start the server
@myapp.get('/')
def index():
    return {'data' : {'name':'Shaheer'}}

#how to start the server with custom route
@myapp.get('/about')
def about_page():
    return {'data' : 'about-page'}

