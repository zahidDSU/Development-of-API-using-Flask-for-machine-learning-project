from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

#Home Page
@app.route("/")
def home():
    return render_template("home.html")

#About Page
@app.route("/about")
def about():
    return render_template("about.html")

#About Page
@app.route("/contact")
def contact():
    return render_template("contact.html")
#Base page
@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/form", methods=['get', 'post'])
def form():
    if request.method=='GET':
        return render_template("home.html")
    else:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        op = request.form['op']
        if op=='+':
            return render_template('home.html', score=(num1+num2))
        elif op=='-':
            return render_template('home.html', score=(num1-num2))
        elif op=='*':
            return render_template('home.html', score=(num1*num2))
        elif op=='/':
            if num2==0:
                return render_template('home.html', score=f"Divide By Zero Error")
            return render_template('home.html', score=(num1/num2))
        else:
            return render_template('home.html', score="Invalid Operator")

if __name__=="__main__":
    app.run(debug=True)