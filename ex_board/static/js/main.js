console.log(sessionVal)
console.log(boardData)

// 게시판별 아이디: 이름 리스트
let boardIdDict = {}

// postData 받기
setBoardList(boardData)
setPostList(boardData)


document.getElementById('sendPage').addEventListener('click', (e)=>{
    data = {}
    let pageNum = document.getElementById("pageText").value
    alert(pageNum)
    data['pageNum'] = pageNum
    data['boardId'] = boardData['post'][0]['board_id'];
    getPostData(data)

})


// 글쓰기
document.querySelector('#postDiv').addEventListener('click', (e)=>{
    if(e.target.id=="writeBtn"){
        boardId = e.target.parentNode.lastChild.value
        location.href = '/board/write/' + sessionVal['loginUserData']['USER_NO'] + "/" + boardId + "/new"
        // location.href = '/board/write/' + boardId
    }
})

document.querySelector("#leftDiv").addEventListener('click', (e)=>{
    // 로그아웃
    if(e.target.id == 'logoutTd'){
        location.href ='/user/logout'
    }
    // 게시판에 따른 게시글 가져오기
    if(e.target.matches("td")){
        data = {}
        data['boardId'] = e.target.id
        getPostData(data)
    }
})

//게시글로 이동
document.querySelector("#postTable").addEventListener('click', (e)=>{
    if(e.target.matches("td")){
        boardCommonNo = e.target.parentNode.firstChild.lastChild.value
        // alert(boardCommonNo)
        if(boardCommonNo=='deleted'){
            alert('이미 삭제된 게시물 입니다.')
        }
        else{
            location.href = '/board/content/' + boardCommonNo
        }
    }
})
// 게시글로 



// 게시글, 게시판 목록 가져오기
function getPostData(bodyData){
    
    console.log(bodyData)
    let rootUrl =  'http://192.168.0.53:5300';
    let routing = '/board/getPost'
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
        setBoardList(res)
        setPostList(res)
        
    })
}



// 게시판 목록 넣기
function setBoardList(boardData){
    console.log(boardData['board'])
    let boardTable = document.getElementById("boardTable")
    
    // 테이블 초기화
    let temp = document.getElementById("boardTable").lastChild
    let newTd = document.createElement('td')
    temp.parentNode.replaceChild(newTd, temp)
    
    boardTable.innerHTML = "<colgroup>" +
    "<col width=100%>" +
    "</colgroup>"
    
    for(i=0; i<boardData["board"].length; i++){
        // 새 행 추가
        let tableRow = boardTable.insertRow();
        
        // 새 행에 cell 추가
        let cell0 = tableRow.insertCell(0);
        
        cell0.innerHTML = boardData['board'][i]['BOARD_NAME'] + "게시판"
        
        cell0.id = boardData['board'][i]['BOARD_ID']
        
        // boardIdDict 만들기
        boardIdDict[boardData['board'][i]['BOARD_ID']] = boardData['board'][i]['BOARD_NAME']
        
        
    }
    
}

// 게시글 목록 넣기
function setPostList(boardData){
    
    console.log(boardData['post'])
    console.log(boardData['post'].length)

    // //페이징
    // let totalPageNum = Math.ceil(parseInt[boardData['totalPage']]/10)
    // let pageTable = document.getElementById("pageTable")
    // // pageTable.innerHTML = "<colgroup>" +
    // //                             "<col width=2%>" +
    // //                             "<col width=2%>" +
    // //                             "<col width=10%>" +
    // //                             "<col width=3%>" +
    // //                             "<col width=10%>" +
    // //                             "<col width=10%>" +
    // //                         "</colgroup>"

    // // 테이블 초기화
    // let temp = document.getElementById("pageTable").lastChild
    // let newTd = document.createElement('td')
    // temp.parentNode.replaceChild(newTd, temp)

    // for(w=0; w<totalPageNum; w++){

    //     // 새 행 추가
    //     let tableRow = pageTable.insertRow();

    //     // 새 행에 cell 추가
    //     let cell0 = tableRow.insertCell(w);
    //     let cell1 = tableRow.insertCell(1);
    //     let cell2 = tableRow.insertCell(2);
    //     let cell3 = tableRow.insertCell(3);
    //     let cell4 = tableRow.insertCell(4);
    //     let cell5 = tableRow.insertCell(5);
    //     let cell6 = tableRow.insertCell(6);
    //     let cell7 = tableRow.insertCell(7);
    // }



    writeDiv = document.getElementById('writeDiv')
    writeDiv.innerHTML = "<h4>" + boardIdDict[boardData['post'][0]['board_id']] + "게시판</h4>" + 
    "<input type=button id='writeBtn' value='글쓰기'></input>" + 
    "<input type=hidden value='" + boardData['post'][0]['board_id'] + "'>"

    // 테이블 초기화
    let temp = document.getElementById("postTable").lastChild
    let newTd = document.createElement('td')
    temp.parentNode.replaceChild(newTd, temp)

    // document.getElementById("#postDiv").innerHTML = boardData['post'][0]['board_name'] + "게시판"s

    // 추가할 table element 찾기
    let postTable = document.getElementById("postTable")
    // let rowCount = postTable.rows.length;
    // let tableRow = postTable.insertRow(rowCount);
    
    postTable.innerHTML = "<colgroup>" +
                                "<col width=2%>" +
                                "<col width=2%>" +
                                "<col width=10%>" +
                                "<col width=3%>" +
                                "<col width=10%>" +
                                "<col width=10%>" +
                            "</colgroup>"



    // let postRows =''
    for(i=0; i<boardData['post'].length; i++){
        
        // 새 행 추가
        let tableRow = postTable.insertRow();
        
        // 새 행에 cell 추가
        let cell0 = tableRow.insertCell(0);
        let cell1 = tableRow.insertCell(1);
        let cell2 = tableRow.insertCell(2);
        let cell3 = tableRow.insertCell(3);
        let cell4 = tableRow.insertCell(4);
        let cell5 = tableRow.insertCell(5);
       
        let rePost = ''
        for(j=1; j<=boardData['post'][i]['depth']; j++){
            rePost = rePost + 're-'
        }
        
        if(boardData['post'][i]['board_common_modidate']==null){
            boardData['post'][i]['board_common_modidate'] = '-'
        }
        // 시간변환
        // else{
        //     let modiDate = get_date_str_gubun(boardData['post'][i]['board_common_modidate'], '-')
        // }

        if(boardData['post'][i]['depth']>0){
            boardData['post'][i]['ROWNUM'] = ''
        }
        
        if(boardData['post'][i]['board_common_del']==1){
            cell2.innerHTML = "삭제된 글입니다."
            cell2.style = "background-color: pink;"
            
            cell0.innerHTML = boardData['post'][i]['ROWNUM'] +
            // "<input type='hidden' class='postTd' value=" + boardData['post'][i]['depth'] + ">" + 
            "<input type='hidden' value=" + boardData['post'][i]['user_no'] + ">" +
            "<input type='hidden' value='deleted'>"
            cell1.innerHTML = boardData['post'][i]['board_common_count']
        }
        else{
            cell2.innerHTML = "<span>" + rePost + "</span>" + boardData['post'][i]['board_common_title']

            cell0.innerHTML = boardData['post'][i]['ROWNUM'] +
            // "<input type='hidden' class='postTd' value=" + boardData['post'][i]['depth'] + ">" + 
            "<input type='hidden' value=" + boardData['post'][i]['user_no'] + ">" +
            "<input type='hidden' value=" + boardData['post'][i]['board_common_no'] + ">"
            cell1.innerHTML = boardData['post'][i]['board_common_count']
        }
        cell3.innerHTML = boardData['post'][i]['user_id']
        // 시간 변환
        // let regDate = get_date_str_gubun(boardData['post'][i]['board_common_regdate'], '-')
        // cell4.innerHTML = regDate
        // cell5.innerHTML = modiDate

        cell4.innerHTML = boardData['post'][i]['board_common_regdate']
        cell5.innerHTML = boardData['post'][i]['board_common_modidate']

        //     let postRow = "<tr>" + 
    //                     "<input type='hidden' value=" + boardData['post'][i]['board_common_id'] + "/>" +
    //                     "<input type='hidden' value=" + boardData['post'][i]['user_no'] + "/>" +
    //                     "<td>" + boardData['post'][i]['board_common_no'] + "</td>" + 
    //                     "<td>" + boardData['post'][i]['board_common_count'] + "</td>" + 
    //                     "<td>" + boardData['post'][i]['board_common_title'] + "</td>" + 
    //                     "<td>" + boardData['post'][i]['user_id'] + "</td>" + 
    //                     "<td>" + boardData['post'][i]['board_common_regdate'] + "</td>" + 
    //                     "<td>" + boardData['post'][i]['board_common_modidate'] + "</td>" + 
    //                   "</tr>"
    //     postRows = postRows + postRow
    }
// console.log(postRows)

}



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
            // location.href = ''

        }else if(res["resultDB"]=='-1'){
            console.log("로그인 실패: 비밀번호 불일치")
            alert("비밀번호가 다릅니다.")
        }

    })
}
function get_date_str_gubun(date, gubun)
{
    var sYear = date.getFullYear();
    var sMonth = date.getMonth() + 1;
    var sDate = date.getDate();

    sMonth = sMonth > 9 ? sMonth : "0" + sMonth;
    sDate  = sDate > 9 ? sDate : "0" + sDate;
    return sYear + gubun + sMonth + gubun + sDate;
}