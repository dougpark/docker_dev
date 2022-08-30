# app.py
# https://medium.com/bitcraft/docker-composing-a-python-3-flask-app-line-by-line-93b721105777

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world! Im on docker_dev'
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=6001)