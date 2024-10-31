from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def getting():
    family_members = ['Akmal', 'Shahriniso', 'Sobirjon', 'Rayhona']
    return render_template('family members.html', family_members=family_members)

if __name__ == '__main__':
    app.run(debug=True)