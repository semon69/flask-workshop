from flask import Flask, render_template, request

app = Flask('app', template_folder='template')

@app.route('/', methods = ['GET'] )

def run ():
    return render_template('index.html')


@app.route('/login', methods = ['GET'] )

def login ():
    
    return "Nothing"

app.run(port = 8080, debug = True)