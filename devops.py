from flask import Flask 

app = Flask(__name__)

@app.route('/info')
def home():
    return "Hello, My name is shubham. This is my 1st project."

@app.route('/address')
def address():
    return "I am from Mumbai, Maharashtra, India"


if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000, debug=True)

