from flask import Flask, render_template, request
from detector import check_request

app = Flask(__name__)

@app.route("/")
def home():
    ip = request.remote_addr

    if check_request(ip):
        return "<h1>403 Forbidden</h1><p>DDoS Attack Detected! Access Blocked.</p>", 403

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)