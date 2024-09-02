import os
from flask import Flask, render_template, request, send_from_directory
from ai import get_fallacies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()

    if data is None:
      return {"error": "Invalid JSON"}, 400

    ai_magic = get_fallacies(data["text"])
    # TODO: handle case where we exceed token limit and incomplete json is returned

    return ai_magic, 200
