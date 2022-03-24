from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def acceuil():
    return render_template('acceuil.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')