console.log(writeData)

// 작성 버튼 클릭 이벤트
document.getElementById("submitBtn").addEventListener("click", (e)=>{

    let boardCommonTitle = document.getElementById("boardCommonTitle").value
    let boardCommonContent = document.getElementById("boardCommonContent").value
    
    writeData["boardCommonTitle"] = boardCommonTitle
    writeData["boardCommonContent"] = boardCommonContent
    
    insertData(writeData)
})


// 게시글 DB 입력
function insertData(bodyData){

    let rootUrl = 'http://192.168.0.53:5300';
    let routing = "/board/insertContent"
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
            alert("작성 완료")
            location.href = "/board/post/" + res["boardId"]
        }else if(res["resultDB"]=='500'){
            alert("작성 실패")
        }
    })
}