from flask import Flask, render_template, request
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("template/index.html")
@app.route("/get", methods=["GET", "POST"])
def chatbot_response():
    user_text = request.args.get('msg')
    return str(get_response(user_text))

if __name__ == "__main__":
    app.run()
