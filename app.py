"""Greeting application module."""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.after_request
def set_x_frame_options(response):
    """Set X-Frame-Options header to prevent clickjacking."""
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'  # Change to 'DENY' if you want to disallow all framing
    return response

@app.route("/", methods=["GET", "POST"])
def home():
    """Home route that handles GET and POST requests."""
    greeting = ""
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            greeting = f"Hello, {name}!"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)
