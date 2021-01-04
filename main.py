from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello, oaisdoasjdold"

@app.route('/test')
def so():
  return "test"

if __name__ == '__main__': 
  app.run()
