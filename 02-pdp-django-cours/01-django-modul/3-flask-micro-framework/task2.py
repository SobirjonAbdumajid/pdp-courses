from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def rendergich():
    return render_template('hello_world.html')

if __name__ == '__main__':
    app.run(debug=True)