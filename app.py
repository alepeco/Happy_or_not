from flask import Flask, request, url_for
from flask.helpers import send_file
app = Flask(__name__, static_url_path='/', static_folder='web')

@app.route("/")
def hello_world():
    return send_file("web/index.html")

@app.route("/sentiment")
def sentiment_analysis():
    text = request.args.get('text', '')
    if len(text) < 8:
        image_url = url_for('static', filename='happy.jpg')
        response = f"Nice! <br><img src='{image_url}' alt='Nice Image' />"
    else:
        image_url = url_for('static', filename='mad.jpg')
        response = f"Wrong! 8 characters or more detected! <br><img src='{image_url}' alt='Wrong Image' />"
    return response
