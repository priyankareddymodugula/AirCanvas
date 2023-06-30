

from flask import Flask, render_template
import air_canvas
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  air_canvas.air_canvas()
  print ('I got clicked!')

  return render_template('finish.html')

if __name__ == '__main__':
  app.run(debug=True)
