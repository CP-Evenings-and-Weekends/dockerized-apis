from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/time")
def time():
    return {"current_time": str(datetime.datetime.now())}


# Add at least one new endpoint of your own below.
# Make it return JSON.  Get creative — quotes, jokes, a counter, anything.


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
