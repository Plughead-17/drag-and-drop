from flask import Flask, request, abort, render_template
import os
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route("/dnd")
def drop():
    return "dnd"

if __name__ == '__main__':
#    host_name = os.uname()[1]
    app.run(debug=True)