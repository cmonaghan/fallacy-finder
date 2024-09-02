from flask import Flask, render_template, request
from ai import get_fallacies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()

    if data is None:
      return {"error": "Invalid JSON"}, 400

    ai_magic = get_fallacies(data["text"])

    return ai_magic, 200
