from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # renders the template 'index.html' from "templates" folder
    return render_template('index.html')

@app.route('/<string:name>')
def hello(name):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)