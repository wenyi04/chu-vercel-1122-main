from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "11/22 中華大學大家好~"

@app.route("/test")
def test():
    return "test 11/22"
    
if __name__ == "__main__":
    app.run()
