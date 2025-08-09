from flask import Flask, render_template

app = Flask(__name__, template_folder='temp')

@app.route("/")
def home():
    return render_template("exe.html")

if __name__ == "__main__":
    app.run(debug=True)