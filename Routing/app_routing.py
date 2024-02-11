# basic flask app 
from flask import Flask

app = Flask(__name__)

#  define a route with the dynamic paremeter 'id' of type int
@app.route('/post/<int:id>')
def show_post(id):
    return f'the Post Id :- {id}'
    


# define a route with the dynamic paremeter ''username' of type string
@app.route('/user/<username>')
def show_user(username):
    return f'User Name :- {username}'

#define a route with /hello 
@app.route('/hello')
def hello():
    return 'Hello World'

# define a  defult route '/'
@app.route('/')
def index():
    return 'Home Page'


if __name__ == '__main__':
    app.run(debug=True)
    

