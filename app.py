from flask import Flask, request, jsonify, render_template
from scripts.gptj_server import gptj_response

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt", "")
    response = gptj_response(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989)
