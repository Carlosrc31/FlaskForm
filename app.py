from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def hello():
    if request.method == "POST":
        isFail = True
        user = request.form.get('user')
        newU = (user == user.capitalize())
        password = request.form.get('pass')
        newP = (password.isalnum()) and (not password.isalpha()) and (not password.isnumeric())
        if newP and newU:
            return render_template('success.html', message = user)
        else:
            fail_txt = "*Debes incluir letra mayúscula al inicio del username y la password debe contener letras y números"
            return render_template('index.html', message = fail_txt)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)