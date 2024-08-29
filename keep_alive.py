from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'CONNECT', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'TRACE', 'HEAD'])

def keep_alive():
  app.run()
