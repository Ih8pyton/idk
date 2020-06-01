import flask
from flask import Flask, request, render_template
from gcd_n_big_gcd import gcd, big_gcd

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/gcd', methods=['GET', 'POST'])
def gcd ():
    a_1 = request.form.get('a')
    b_1 = request.form.get('b')

    if a_1 == None:
        a_1 = 1

    if b_1 == None:
        b_1 = 1
        
    a_2 = int(a_1)
    b_2 = int(b_1)

    return flask.render_template(
        'gcd.html',
        a=a_1,b=b_1,
        Gcd=big_gcd(a_2,b_2),
        method=request.method
    )


if __name__ == '__main__':
   app.run(debug = True)
