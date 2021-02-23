console.log(contentData)
console.log(sessionVal['loginUserData'])
console.log(contentData['reply'])

let clickedPid = ''

// main으로 이동
let conDiv = document.querySelector("#conDiv h4")
conDiv.addEventListener('click', (e)=>{
    data1 = contentData['content'][0]['BOARD_ID']
    location.href = '/board/post/'+ data1
    
})



// 내용 넣기
setContentPage(contentData)
// 댓글 넣기
setReplyPage(contentData)
// 대댓글 작성을 위한 pid 설정    
document.querySelector("#reTable").addEventListener('click', (e)=>{
    
    if(e.target.matches("td")){
       
        // e.target.parentNode.classList.toggle("clicked")
        clickedPid = e.target.parentNode.firstChild.lastChild.value
        if(clickedPid=="deleted"){
            alert("삭제된 댓글입니다.")
            clickedPid = ''
        }else{
            userId = e.target.parentNode.firstChild.firstChild.value
            console.log(clickedPid)
            document.getElementById('spanH4').innerHTML = "<h4 id='h4'>" + userId + "에 댓글" + "<input type='button' id=removeClickedId value='X'></h4>" + 
            "<input type='hidden' id='boardCommentPId' value='" + clickedPid + "'/>"
        }

    }else{
  
        temp = document.getElementById('spanH4').lastChild
        let newSpan = document.createElement('span')
        temp.parentNode.replaceChild(newSpan, temp)
        clickedPid = ''
        userId=''
        document.getElementById('spanH4').innerHTML = "<h4>댓글</h4>" + 
        "<input type='hidden' id='boardCommentPId' value='0'/>"
    }

})
// 댓글 대상 취소
document.querySelector("#replyDiv2").addEventListener('click', (e)=>{
    if(e.target.matches("#removeClickedId")){
        temp = document.getElementById('spanH4').lastChild
        let newSpan = document.createElement('span')
        temp.parentNode.replaceChild(newSpan, temp)
        clickedPid = ''
        userId=''
        document.getElementById('spanH4').innerHTML = "<h4>댓글</h4>" + 
        "<input type='hidden' id='boardCommentPId' value='0'/>"
    }
})

// 댓글 작성
document.getElementById("commentBtn").addEventListener("click", (e)=>{
    data = {}
    replyContent = document.getElementById("textArea").value
    boardCommentPId = document.getElementById("boardCommentPId").value
    boardCommonNo = contentData['content'][0]['BOARD_COMMON_NO']
    data['userNo'] = sessionVal['loginUserData']['USER_NO']
    data['boardCommentContent'] = replyContent
    data['boardCommentPid'] = boardCommentPId
    data['boardCommonNo'] = boardCommonNo
    if(replyContent==''){
        alert("내용을 입력해주세요")
    }else{
        // alert(data['boardCommentPid'])
        insertReply(data)
    }
})
function insertReply(bodyData){
    let rootUrl =  'http://192.168.0.53:5300';
    let routing = '/board/comment/insertData'
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
            alert("댓글 작성완료")
            location.href = '/board/content/' + contentData['content'][0]['BOARD_COMMON_NO']
        }else if(res["resultDB"]=='500'){
            alert("댓글 실패")
        }
    })


}


// 댓글 삭제하기
if(contentData['reply'].length>0){

    document.getElementById("reTable").addEventListener('click', (e)=>{
        if(e.target.matches('.reDel')){        
            bodyData = {}
            boardCommentId = e.target.parentNode.parentNode.firstChild.lastChild.value
            boardCommonNo = contentData['reply'][0]['board_common_no']
            bodyData['boardCommentId'] = boardCommentId
            bodyData['boardCommonNo'] = boardCommonNo
            let routing = '/board/comment/del'
            let word = {}
            word['success'] = '댓글 삭제완료'
            word['fail'] = '댓글 삭제실패'

            conDB(routing, bodyData, word)   
        }    

        if(e.target.matches('.reModi')){      
            bodyData = {}
            boardCommentId = e.target.parentNode.parentNode.firstChild.lastChild.value
            alert(boardCommentId)
            boardCommonNo = contentData['reply'][0]['board_common_no']
            bodyData['boardCommentId'] = boardCommentId
            bodyData['boardCommonNo'] = boardCommonNo
            let routing = '/board/comment/del'
            let word = {}
            word['success'] = '댓글 삭제완료'
            word['fail'] = '댓글 삭제실패'
    
            // conDB(routing, bodyData, word)   
            }    
    




})


}
function conDB(routing, bodyData, word){
    let rootUrl =  'http://192.168.0.53:5300';
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
            alert(word['success'])
            location.href = '/board/content/' + contentData['reply'][0]['board_common_no']
        }else if(res["resultDB"]=='500'){
            alert(word['fail'])
        }
    })
}




if (sessionVal['loginUserData']['AUTH_TYPE'] == 1 || sessionVal['loginUserData']['USER_NO']==contentData['content'][0]['USER_NO']){

// 삭제하기
document.getElementById("delBtn").addEventListener('click', (e)=>{
    bodyData = {}
    boardCommonNo = contentData['content'][0]['BOARD_COMMON_NO']
    boardId = contentData['content'][0]['BOARD_ID']
    bodyData['boardCommonNo'] = boardCommonNo
    bodyData['boardId'] = boardId
    // location.href = '/board/del/' + boardCommonNo
    console.log(bodyData)
    let rootUrl =  'http://192.168.0.53:5300';
    let routing = '/board/deletePost'
    fetch(rootUrl + routing, {
        method : 'DELETE',
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
            alert("삭제 완료")
            location.href = "/board/post/" + res["boardId"]
        }else if(res["resultDB"]=='500'){
            alert("삭제 실패")
        }
    })
})


// 수정하기
document.getElementById("modiBtn").addEventListener('click', (e)=>{
    boardCommonNo = contentData['content'][0]['BOARD_COMMON_NO']
    location.href = '/board/getBoardToModi/' + boardCommonNo
})

}
// 답글달기
document.getElementById("rePostBtn").addEventListener("click", (e)=>{
    boardId = contentData['content'][0]['BOARD_ID']  
    boardCommonPno = contentData['content'][0]['BOARD_COMMON_NO']
    location.href = '/board/write/' + sessionVal['loginUserData']['USER_NO'] + "/" + boardId + "/" + boardCommonPno
})

// 내용 넣기
function setContentPage(data){
    console.log(data['content'])
    let conTable = document.getElementById("conTable")
    
    
    // 테이블 초기화
    let temp = document.getElementById("conTable").lastChild
    let newTd = document.createElement('td')
    temp.parentNode.replaceChild(newTd, temp)
  
    conTable.innerHTML = "<colgroup>" +
                                "<col width=5%>" +
                                "<col width=80%>" +
                            "</colgroup>"

    for(i=0; i<data["content"].length; i++){
        
        if(data['content'][i]['BOARD_COMMON_MODIDATE']==null){
            data['content'][i]['BOARD_COMMON_MODIDATE'] = '-'
        }

        // 새 행 추가
        let titleRow = conTable.insertRow(0);
        let writerRow = conTable.insertRow(1);
        let regDateRow = conTable.insertRow(2);
        let modiDateRow = conTable.insertRow(3);
        let contentRow = conTable.insertRow(4);
        contentRow.id = 'conTr'
        

        
        // 새 행에 cell 추가
        let title0 = titleRow.insertCell(0);
        let title1 = titleRow.insertCell(1);
        title1.id = 'boardCommonId'
        title0.innerHTML = "제목"
        title1.innerHTML = data['content'][i]['BOARD_COMMON_TITLE'] + '&nbsp' +
        "<input type='button' id='rePostBtn' value='답글달기'>" +
        "<input type='hidden' value=" + data['content'][i]['BOARD_COMMON_ID'] + ">"

        let writer0 = writerRow.insertCell(0);
        let writer1 = writerRow.insertCell(1);
        writer1.id = 'user_no'
        writer0.innerHTML = '작성자'
        writer1.innerHTML = data['content'][i]['USER_ID'] +
        "<input type='hidden' value=" + data['content'][i]['USER_NO'] + ">"

        let regDate0 = regDateRow.insertCell(0);
        let regDate1 = regDateRow.insertCell(1);
        regDate0.innerHTML = "등록일"
        regDate1.innerHTML = data['content'][i]['BOARD_COMMON_REGDATE']

        let modiDate0 = modiDateRow.insertCell(0);
        let modiDate1 = modiDateRow.insertCell(1);
        modiDate0.innerHTML = "수정일"
        modiDate1.innerHTML = data['content'][i]['BOARD_COMMON_MODIDATE']
         
         let content0 = contentRow.insertCell(0);
         let content1 = contentRow.insertCell(1);
         content1.id = 'boardCommonPno'
         content0.innerHTML = "내용"
         content1.innerHTML = data['content'][i]['BOARD_COMMON_CONTENT'] +
         "<input type='hidden' value=" + data['content'][i]['BOARD_COMMON_PNO'] + ">"

         // 작성자는 수정, 삭제 가능
         
         if(sessionVal['loginUserData']['AUTH_TYPE'] == 1 || sessionVal['loginUserData']['USER_NO']==data['content'][i]['USER_NO']){
            modiDate1.innerHTML = data['content'][i]['BOARD_COMMON_REGDATE'] + '&nbsp' + 
            "<input type='button' id='modiBtn' value='수정하기'/>" + '&nbsp' +
            "<input type='button' id='delBtn' value='삭제하기'/>"
         }
    }
}    

// 댓글 넣기
function setReplyPage(data){
    console.log(data['reply'])

    // data['reply'][0]['BOARD_COMMON_NO']
    let reTable = document.getElementById("reTable")
    
    
    // 테이블 초기화
    let temp = document.getElementById("reTable").lastChild
    let newTd = document.createElement('td')
    temp.parentNode.replaceChild(newTd, temp)
  
    reTable.innerHTML = "<colgroup>" +
                                "<col width=7%>" +
                                "<col width=43%>" +
                                "<col width=50%>" + 
                            "</colgroup>"

    for(i=0; i<data["reply"].length; i++){

        // 새 행 추가
        let tableRow = reTable.insertRow();
        
        // 새 행에 cell 추가
        let cell0 = tableRow.insertCell(0);
        let cell1 = tableRow.insertCell(1);
        let cell2 = tableRow.insertCell(2);
        let cell3 = tableRow.insertCell(3);
        // let cell4 = tableRow.insertCell(4);
        // let cell5 = tableRow.insertCell(5);

        let rePost = ''
        let rePost2 = ''
        for(j=1; j<=data['reply'][i]['depth']; j++){
            rePost = rePost + '&nbsp&nbsp'
            rePost2 = rePost2 + '&nbsp&nbsp'

        }
        if(data['reply'][i]['depth']>0){
            rePost = rePost + 'ㄴ'
        }
        if(data['reply'][i]['board_comment_del']==1){
            cell1.innerHTML = "<span>" + rePost2 + "</span>" + "삭제된 댓글입니다."
            cell1.style = "background-color: pink;"

            // userIdVal = '2' + data['reply'][i]['user_id'] 
            // cell0.innerHTML = "<span>" + rePost + "</span>" + userIdVal +
            cell0.innerHTML = "<span>" + rePost + "</span>" + data['reply'][i]['user_id'] +
            // "<input type='hidden' class='postTd' value=" + data['post'][i]['depth'] + ">" + 
            "<input type='hidden' value=" + data['reply'][i]['user_no'] + ">" +
            "<input type='hidden' value='deleted'>"
            cell0.style = "text-align: center;"
        }
        else{
            cell1.innerHTML = "<span>" + rePost2 + "</span>" + data['reply'][i]['board_comment_content']

            cell0.innerHTML = 
            "<input type='hidden' value=" + data['reply'][i]['user_id'] + ">" +
            "<span>" + rePost + "</span>" + data['reply'][i]['user_id'] +
            // "<input type='hidden' class='postTd' value=" + data['post'][i]['depth'] + ">" + 
            "<input type='hidden' value=" + data['reply'][i]['user_no'] + ">" +
            "<input type='hidden' value=" + data['reply'][i]['board_comment_id'] + ">"
        }

        // 수정유무에 따른 수정일 또는 등록일 표기
        if(data['reply'][i]['board_comment_modidate']==null){
            
            // 작성자, 관리자는 수정/삭제 가능
            if(sessionVal['loginUserData']['AUTH_TYPE'] == 1 || sessionVal['loginUserData']['USER_NO']==data['reply'][i]['user_no']){
                if(data['reply'][i]['board_comment_del']==0){

                    cell2.innerHTML = "작성일: " + data['reply'][i]['board_comment_regdate'] + '&nbsp' + 
                    // "<input type='button' class='reModi' value='수정하기'/>" + '&nbsp' +
                    "<input type='button' class='reDel' value='삭제하기'/>"
                }else{
                    cell2.innerHTML = "작성일: " + data['reply'][i]['board_comment_regdate'] + '&nbsp'
                }
            }else{
                cell2.innerHTML = "작성일: " + data['reply'][i]['board_comment_regdate'] + '&nbsp'

            }
        }
        else{

            // 작성자, 관리자는 수정/삭제 가능
            if( sessionVal['loginUserData']['AUTH_TYPE'] == 1 || sessionVal['loginUserData']['USER_NO']==data['reply'][i]['user_no']){
                if(data['reply'][i]['board_comment_del']==0 ){
                    cell2.innerHTML = "수정일: " + data['reply'][i]['board_comment_modidate'] + '&nbsp' +
                    // "<input type='button' class='reModi' value='수정하기'/>" + '&nbsp' +
                    "<input type='button' class='reDel' value='삭제하기'/>"
                }
                else{
                    cell2.innerHTML = "수정일: " + data['reply'][i]['board_comment_modidate'] + '&nbsp'
                }
            }
            else{
                cell2.innerHTML = "수정일: " + data['reply'][i]['board_comment_modidate'] + '&nbsp'
            }

        }
        
    }
}    