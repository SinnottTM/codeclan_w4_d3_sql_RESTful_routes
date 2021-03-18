# app.py is the controller of the app (the brain) and allows flask to activate, which sets up a local server with a webpage for us to view the app running. 
# 
# To run, use flask run in the terminal. To quit, use control+c.
# 
# This also allows the user to make inputs, which (almost always) is the whole point of any app
# 
# VITAL part of any app

from flask import Flask, render_template
# bring the controller to the main app with this import
from controllers.task_controller import tasks_blueprint
app = Flask(__name__)

# connect the controller to the main app with this function
app.register_blueprint(tasks_blueprint)

# basic route, establishes access to the index page of HTML
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
