from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello,Dilip , World Test Sushant !!!!!! from GitHub Actions + Dockerr"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
