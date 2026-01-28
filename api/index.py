from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Mengizinkan website mengakses data dari domain berbeda

@app.route('/')
def home():
    return "API is running!"

# Sisanya adalah kode asli dari moviebox-api...
