## import flask----------------

from flask import Flask


## Instantiate the Flask app ------------------------

app = Flask(__name__)

## Home Route -----------------------------

@app.route('/')
def hello():
    return 'Hello my name is azaz'

# if you want to run this app , you call the run()

if __name__ == '__main__':
    app.run(debug=True)
