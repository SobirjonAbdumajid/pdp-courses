from datetime import datetime
from flask import Flask, request, redirect, render_template, make_response, session
# import datetime

app = Flask(__name__) # opening application
app.secret_key = 'secret'

@app.route('/home')  # rout berish. brouzerga shuni berish orqali kiradigan bo'lsa
def home(): # shu funksiyani tepadagi routega registratsiya qiladi
    return """
    <h1>it is homw page</h1>
    <a href='/home'>about page</a?>
"""

@app.route('/time')
def time():
    return str(datetime.now())

@app.route('/about')
def about():
    return """
    <h1>it is about page</h1>
    <a href='/home'>home page</a?>
"""

# @app.route('/greet/<name>')
# def greet(name):
#     return f"""
#     <h1>Hello, {name} </h1>
# """

@app.route('/greet')
def greet():
    variable = request.args.get('name', 'World')
    return f"""
    <h1>Hello, {variable}</h1>
""", 404

@app.route('/search')
def searchfunk():
    q = request.args.get('q')
    if not q:
        return f'''
        <form>
            <input name="q"/>
            <button type="submit">Send</button>
        </form>
    '''
    return redirect(f"http://google.com/search?q={q}") # agar 404 tururadi Redirecting... deb

@app.route('/register', methods=['GET', 'POST'])
def register():

    if 'registered' in request.cookies:
        # return render_template('success.html', name=request.cookies['name'])
        return render_template('success.html', name=session['name'])

    if request.method == 'GET':
        return render_template('register.html')
    
    if int(request.form['age']) < 12:
        return render_template('error.html')

    name = request.form['name']

    cv = request.files['cv']
    cv.save(f'uploads/{name}_cv.png')

    response = make_response(
        render_template('success.html', name=name)
    )

    response.set_cookie('name', name)
    session['name'] = name
    response.set_cookie('registered', 'true')

    return response


if __name__ == '__main__':
    app.run(debug=True) # port host berish mumkin