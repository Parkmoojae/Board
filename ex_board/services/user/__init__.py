from services import app
from flask import request, jsonify, render_template, session, redirect
from services.user import service as userService

# @app.route("/signUp")
# def signUpLandPage():
#     return render_template("signUp.html")

@app.route("/user/signUp", methods=["POST"])
def signUp():
    print('sendUserData 도착')
    result = {}
    data = request.get_json()
    print("sendUserData: ", data)
    # checkIdVal = signUpService.checkId(data['userId'])
    result["resultDB"] = userService.userInsert(data)
    print("@@@@@@@@@")
    print(result)
    print("@@@@@@@@@")
    return jsonify(result)

@app.route("/user/login", methods=["POST"])
def login():
    print("login 도착")
    result = {}
    data = request.get_json()
    resultService = userService.userLogin(data)
    print(result)
    print(type(result))

    if(len(resultService) == 0):
        # 아이디 없음
        result['resultDB'] = '0'
    elif(resultService[0]['USER_PW'] == data['userPw']):
        # 로그인 성공
        loginUpdate = userService.userLastlogin(resultService[0]['USER_NO'])
        
        if(loginUpdate=='200'):
            result['resultDB'] = '1'
        
        # 로그인 후 세션에 저장
        session["loginUserData"] = resultService[0]
    else:
        # 비밀번호 불일치
        result['resultDB'] = '-1'
    
    return result
    
@app.route("/user/sessionCheck")
def sessionCheck():
    print(session.get("loginUserData"))
    return session.get("loginUserData")

@app.route("/user/logout")
def logout():
    session.pop("loginUserData", None)
    # return render_template("/")
    return redirect('/render/login')