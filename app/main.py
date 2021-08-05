from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
  return 'Hello World from Flask!!!'

@app.route('/subpath_a')
def subpath_a():
  return 'This is subpath_a'

@app.route('/subpath_b')
def subpath_b():
  return 'This is subpath_b'

@app.route('/subpath_a/subpath_a_1')
def subpath_a_1():
  return 'This is subpath_a/subpath_a_1'

@app.route('/subpath_a/subpath_a_2')
def subpath_a_2():
  return 'This is subpath_a/subpath_a_2'

@app.route('/subpath_b/subpath_b_1')
def subpath_b_1():
  return 'This is subpath_b/subpath_b_1'

@app.route('/subpath_b/subpath_b_2')
def subpath_b_2():
  return 'This is subpath_b/subpath_b_2'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
