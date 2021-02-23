from services import app
from flask import request, jsonify, render_template, session

# 로그인 render 페이지
@app.route('/render/login')
def renderLogin():
    return render_template('login.html')

# 회원가입 render 페이지
@app.route("/render/signUp")
def renderSignUp():
    return render_template("signUp.html")