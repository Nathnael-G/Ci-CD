"""Greeting application module."""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.after_request
def set_security_headers(response):
    """Set security headers to prevent clickjacking and content type sniffing."""
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'  # Prevents clickjacking
    response.headers['X-Content-Type-Options'] = 'nosniff'  # Prevents MIME type sniffing
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
