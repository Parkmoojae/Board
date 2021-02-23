//회원가입 버튼 클릭 이벤트
document.getElementById('submitBtn').addEventListener('click', function(e){
    userId = document.getElementById('userId').value
    userPw = document.getElementById('userPw').value
    userEmail = document.getElementById('userEmail').value
    url = document.getElementById('url').value
    userEmail = userEmail + '@' + url
    userPhone = document.getElementById('userPhone').value
    radioCheck1 = document.getElementsByName('radioCheck1')
    userSex = ''
    for(var radioCheck of radioCheck1){
        if (radioCheck.checked){
            userSex = radioCheck.value
            break
        }
    }
    userBirth = document.getElementById('userBirth').value
    userAdd = document.getElementById('userAdd').value
    
    let bodyData = {}
    if(userId){
        bodyData['userId'] = userId
    }
    if(userPw){
        bodyData['userPw'] = userPw
    }
    if(userEmail){
        bodyData['userEmail'] = userEmail
    }
    if(userPhone){
        bodyData['userPhone'] = userPhone
    }
    if(userSex){
        bodyData['userSex'] = userSex
    }
    if(userBirth){
        bodyData['userBirth'] = userBirth
    }
    if(userAdd){
        bodyData['userAdd'] = userAdd
    }

    sendData(bodyData)
    
})

function sendData(bodyData){
    console.log(bodyData)
    let rootUrl =  'http://192.168.0.53:5300';
    let routing = '/user/signUp'
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
        if(res["resultDB"]=='200'){
            alert("회원가입 완료")
            location.href = "/render/login"
        }else if(res["resultDB"]=='500'){
            alert("회원가입 실패")
        }
    })

    // .then(function(res){
    //     key = Object.keys(res)
    //     for(i=0; i<key.length; i++){
    //         if(key[i]=="resultDB"){
    //             console.log(key[i] + ": " + res[key[i]])
    //             alert("회원가입 완료")
    //             location.href = "/"
    //         }
    //     }
    // })




    // .then(function(res){
    //     if(res.status === 200 || res.status === 201){
    //         key = Object.keys(res.json());
    //         for(i=0; key.length; i++){
    //             if(key=="resultDB"){
    //                 console.log(key + ": " + res.json()[key[i]]);
    //             }
    //         }
    //         console.log(res.json());
    //     }else{
    //         console.error(res.statusText);
    //     }
    // })

    // .then(data => {console.log(data); return data;})
    // .then(function(data){
    //     return data.json();
    // })
    // .then(function(json){
    //     key = Object.keys(json);
    //     for(i=0; key.length; i++){
    //         if(key[i]=="resultDB"){
    //             alert(key[i] + ": " + json[key[i]])
    //         }
    //     }
    //     console.log(json);
    // })

    // .then(function(response){
    //     response.json().then(function(json){
    //         alert(json);
    //     })
    // })

    // .then(function(response){
    //     response.json().then(function(json){
    //         alert(json);
    //     })
    // })
    

    // .then(response => {console.log(response); return response;})
    // .then(function(a){
    //     return a.json()
    // })
    // .then(function(json){
    //     alert(json)
    // })

    // .then(response => {console.log(response); return response;})
    // .then(function(a){
    //     return a.json();
    // })
    // .then(function(json){
    //     key = Object.keys(json);
    //     for(i=0; i<key.length; i++){
    //         if(key[i] == "error"){
    //             alert(key[i] + ": " + json[key[i]])
    //         }
    //     }
    //     console.log(json);
    // })
}