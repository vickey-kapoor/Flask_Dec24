from flask import Flask

app = Flask(__name__)

# Create API endpoints

@app.route('/', methods=['GET'])
def hello_world():
    # this function will automatically execute
    return "<h1> Hello there !! </h1>"
@app.route('/ping', methods=['GET'])
def ping():
    return {"message": "Why are you pinging me? "}