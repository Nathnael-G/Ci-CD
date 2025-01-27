"""Greeting application module."""

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwertyh1234567'  # Replace with a strong secret key

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Define a form class for handling user input
class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.after_request
def remove_server_header(response):
    """Remove or modify the Server header."""
    response.headers.pop('Server', None)  # Remove the Server header if it exists
    return response

@app.after_request
def set_security_headers(response):
    """Set security headers to prevent clickjacking, 
    content type sniffing, and improve site isolation."""
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'  # Prevents clickjacking
    response.headers['X-Content-Type-Options'] = 'nosniff'  # Prevents MIME type sniffing
    response.headers['Permissions-Policy'] = 'geolocation=(self), microphone=(), camera=()'  # Control feature access
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'  # Enforce COEP
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'  # Enforce COOP
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; object-src 'none'; frame-ancestors 'none'"  # Set CSP
    return response

@app.route("/", methods=["GET", "POST"])
def home():
    """Home route that handles GET and POST requests."""
    form = NameForm()  # Create an instance of the form
    greeting = ""
    
    if form.validate_on_submit():  # Check if the form is submitted and valid
        name = form.name.data  # Get the name from the form data
        if name:
            greeting = f"Hello, {name}!"
    
    return render_template("index.html", form=form, greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)
