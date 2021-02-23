console.log(writeData)

document.getElementById("boardCommonTitle").value = writeData[0]['BOARD_COMMON_TITLE']
document.getElementById("boardCommonContent").value = writeData[0]['BOARD_COMMON_CONTENT']


// 작성 버튼 클릭 이벤트
document.getElementById("submitBtn").addEventListener("click", (e)=>{
    data ={}
    let boardCommonTitle = document.getElementById("boardCommonTitle").value
    let boardCommonContent = document.getElementById("boardCommonContent").value
    data['boardCommonNo']=writeData[0]['BOARD_COMMON_NO']
    data["boardCommonTitle"] = boardCommonTitle
    data["boardCommonContent"] = boardCommonContent
    data["boardId"] = writeData[0]['BOARD_ID']
    console.log(data)
    insertData(data)
})


// 게시글 DB 입력
function insertData(bodyData){

    let rootUrl = 'http://192.168.0.53:5300';
    let routing = "/board/updateContent"
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
            alert("수정 완료")
            location.href = "/board/content/" + res["boardCommonNo"]
        }else if(res["resultDB"]=='500'){
            alert("수정 실패")
        }
    })
}