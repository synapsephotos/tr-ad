from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'


def keep_alive():
  app.run()
