from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main_handler():
   return "coba"

if __name__ == '__main__':
   app.run(port=8888, debug=False)
