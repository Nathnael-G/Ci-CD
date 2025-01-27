"""Greeting application module."""

from flask import Flask, render_template, request
from flask_talisman import Talisman

app = Flask(__name__)

# Set up Talisman with a strict Content Security Policy
csp = {
    'default-src': "'self'",  # Allow content only from the same origin
    'script-src': "'self'",    # Allow scripts only from the same origin
    'img-src': "'self' data:",  # Allow images from the same origin and inline images
    'style-src': "'self' 'unsafe-inline'",  # Allow styles from the same origin and inline styles (be cautious with inline)
    'object-src': "'none'",    # Disallow all object sources
    'frame-ancestors': "'none'" # Prevent any framing of this content
}

Talisman(app, content_security_policy=csp)

@app.after_request
def remove_server_header(response):
    """Remove or modify the Server header."""
    response.headers.pop('Server', None)  # Remove the Server header if it exists
    return response

@app.after_request
def set_security_headers(response):
    """Set additional security headers."""
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
