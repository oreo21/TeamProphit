from flask import Flask, render_template, session, request, redirect, url_for, flash


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    #using students for both rn
    if "username" in session:
        #usertype = #function for getting user type
        #hard coding for now
        usertype = 0
        #if usertype == 0: #change 0 to whatever boolean we set to differentiate
        #blah

        #elif usertype == 1:
        #not the other usertype
        return render_template("stuHome.html", user_type = usertype)
    return render_template("stuLogin.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
