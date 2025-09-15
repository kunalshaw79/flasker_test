from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return '<h1>Hello from Vercel!</h1><p>The deployment is working.</p>'