from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def home():
    return {"status": "ok", "service": "demo-ci-cd"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
