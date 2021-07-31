from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
  return 'Hello World from Flask!!!'

@app.route('/home')
def home():
  return 'This is a home page.'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=10000)
