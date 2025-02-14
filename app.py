from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Sentinel-Intel is Running!"

if __name__ == "__main__":
    app.run()