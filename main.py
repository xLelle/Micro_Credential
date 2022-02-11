# build for flask app for project 2
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# connect to database 
app.config ['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:&Sw3LcE$29@localhost/demoDB'
db1 = SQLAlchemy(app) # inistialize the connections to the database on the app

# submit order database defined
class Submit(db1.Model):
    __tablename__ = "submit"
    id=db1.Column(db1.Integer, primary_key=True)
    email = db1.Column(db1.String(120), unique = True)
    username = db1.Column(db1.String(120))

    def __init__(self,email, username):
        self.email = email
        self.username = username

@app.route("/")

def submit():
    return render_template("checkout.html")

# get info from your form in checkout.html when the submit button is clicked
@app.route('/', methods=['POST'])
def thankyou():
    if request.method == "POST":
        email = request.form["emailAddress"]
        username = request.form["username"]
        print(request.form)
    #last step: commit 
    submit = Submit(email,username)
    db1.session.add(submit)
    db1.session.commit() # execute
    return render_template('thankyou.html')

      
if __name__ == "__main__":
    app.debug=True
    app.run()