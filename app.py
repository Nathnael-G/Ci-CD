"""Greeting application module."""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.after_request
def set_security_headers(response):
    """Set security headers to prevent clickjacking, content type sniffing, and improve site isolation."""
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'  # Prevents clickjacking
    response.headers['X-Content-Type-Options'] = 'nosniff'  # Prevents MIME type sniffing
    response.headers['Permissions-Policy'] = 'geolocation=(self), microphone=(), camera=()'  # Control feature access
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'  # Enforce COEP
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'  # Enforce COOP
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
