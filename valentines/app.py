from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/question", methods=["GET", "POST"])
def question():
    choice = None
    if request.method == "POST":
        choice = request.form.get("valentine")  # will be "yes" or "no"
    return render_template("question.html", choice=choice)

if __name__ == "__main__":
    app.run(debug=True)
