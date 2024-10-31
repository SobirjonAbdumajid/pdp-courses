from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def print_image():
    return render_template('forimage.html')

if __name__ == '__main__':
    app.run(debug=True)