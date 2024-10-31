from flask import Flask, request

app = Flask(__name__)

@app.route('/somsajon')
def somsa():
    variable = request.args.get('name', 'somsa')
    return f"""
    <h1>Hello, {variable}</h1>
""", 404


if __name__ == "__main__":
    app.run(debug=True)