from flask import Flask, render_template_string, request
import cowsay

app = Flask(__name__)

# HTML template with a basic form
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Cowsay on Flask</title>
    <style>
        body { font-family: monospace; padding: 20px; background: #f9f9f9; }
        textarea { width: 100%; height: 150px; }
    </style>
</head>
<body>
    <h1>Cowsay Web App 🐄</h1>
    <form method="post">
        <label>Enter your message:</label><br>
        <input type="text" name="message" required>
        <br><br>
        <input type="submit" value="Moo!">
    </form>

    {% if output %}
        <h2>Output:</h2>
        <pre>{{ output }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        message = request.form.get("message", "")
        if message:
            output = cowsay.get_output_string("cow", message)
    return render_template_string(HTML_TEMPLATE, output=output)

if __name__ == "__main__":
    app.run(debug=True)