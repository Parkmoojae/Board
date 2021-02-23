// 회원가입 버튼 이벤트(페이지 이동)
document.getElementById('signUpBtn').addEventListener('click', function(e){
    location.href = '/render/signUp'
})
// 로그인 버튼
document.getElementById('loginBtn').addEventListener('click', function(e){
    userId = document.getElementById('loginId').value
    userPw = document.getElementById('loginPw').value
    let bodyData = {}

    // // 유효성 검사(업데이트 예정)
    if(userId){
        bodyData['userId'] = userId
    }
    if(userPw){
        bodyData['userPw'] = userPw
    }

    sendData(bodyData)

})

function sendData(bodyData){
    console.log(bodyData)
    let rootUrl =  'http://192.168.0.53:5300';
    let routing = '/user/login'
    fetch(rootUrl + routing, {
        method : 'POST',
        headers : {
            'Content-type' : 'application/json;charset=utf-8',
        },
        // headers : {},
        body : JSON.stringify(bodyData)
        // body: blob
    })  
    .then(response => {console.log(response); return response;})
    .then(function(temp){
        return temp.json();
    })
    .then(function(res){
        if(res["resultDB"]=='0'){
            console.log("로그인 실패: 아이디 불일치")
            alert("아이디가 불일치 합니다.")

        }else if(res["resultDB"]=='1'){
            console.log("로그인 성공")
            // location.href = '/board/boardcommon'
            // location.href = '/render/main'
            data1 = "boadId"
            pageNum = 1
            location.href = '/board/post/'+ data1 + "/" + pageNum

        }else if(res["resultDB"]=='-1'){
            console.log("로그인 실패: 비밀번호 불일치")
            alert("비밀번호가 다릅니다.")
        }

    })
}