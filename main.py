from flask import Flask, app, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/othody')
def othody():
    return render_template('othody.html')

app.run(debug=True)