from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text
