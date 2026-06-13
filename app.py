from flask import Flask, render_template, request
from responses import responses

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""

    if request.method == "POST":
        user = request.form["message"].lower().strip()
        reply = responses.get(
            user,
            "I don't understand."
        )

    return render_template(
        "index.html",
        reply=reply
    )

if __name__ == "__main__":
    app.run()

    