from services import app
from flask import request, jsonify, render_template, session
from services.board import service as boardService


@app.route('/board/post/<boadId>/<pageNum>')
def boardLand(boadId, pageNum):
    if boadId == "boadId":
        boadId = 101

    
    result = {}
    result["post"] = boardService.postList(boadId, pageNum)
    result["board"] = boardService.boardList()
    result['totalPage'] = boardService.totalPage(boadId)

    print("#######")
    print(result["post"])
    print(type(result["post"]))
    print("#######")

    # view에서는 dict, string, tuple 형태만 가능하여 jsonify로 변환
    # return jsonify(result)

    return render_template("main.html", data=result)


@app.route('/board/getPost', methods=["POST"])
def getPost():
    data = request.get_json()
    print(data)
    result = {}
    result["post"] = boardService.postList(data["boardId"], data['pageNum'])
    result["board"] = boardService.boardList()
    result['totalPage'] = boardService.totalPage(data['boardId'])

    return jsonify(result)

# 게시글 보기
@app.route('/board/content/<boardCommonNo>')
def content(boardCommonNo):
    print("게시글 보기 도착")
    result = {}
    result['content'] = boardService.getContent(boardCommonNo)
    result['reply'] = boardService.getReply(boardCommonNo)
    print(result)
    print(type(result))

    return render_template("content.html", data=result)

# 게시글 작성, 답글 작성 페이지
@app.route('/board/write/<userNo>/<boardId>/<typeData>')
def write(userNo, boardId, typeData):
    result = {}
    result['userNo'] = userNo
    result['boardId'] = boardId
    if typeData=="new":
        result['boardCommonPno'] = 0
    else:
        result['boardCommonPno'] = typeData

    print('write 도착')
    print(userNo)
    print(boardId)
    print(typeData)

    return render_template("writePost.html", data=result)


@app.route("/board/insertContent", methods=["POST"])
def insertContent():
    data = {}
    data = request.get_json()
    print(data)
    result = {}
    result["resultDB"] = boardService.insertContent(data)
    result["boardId"] = data["boardId"]
    return result


@app.route("/board/updateContent", methods=["POST"])
def updateContent():
    data = {}
    data = request.get_json()
    print("업데이트 도착")
    print(data)
    result = {}
    result["resultDB"] = boardService.updateContent(data)
    result["boardCommonNo"] = data["boardCommonNo"]
    return result



@app.route("/board/getBoardToModi/<boardCommonNo>")
def getBoardToModi(boardCommonNo):
    print("수정 도착")
    print(boardCommonNo)
    result = boardService.getBoardToModi(boardCommonNo)

    return render_template('modiPost.html', data=result)


@app.route("/board/deletePost", methods=["DELETE"])
def deletePost():
    data = {}
    data = request.get_json()
    print("삭제 도착")
    print(data)
    result = {}
    result["resultDB"] = boardService.deletePost(data)
    result["boardId"] = data["boardId"]
    return result

@app.route('/board/comment/insertData', methods=['POST'])
def insertComment():
    data={}
    data = request.get_json()
    print("댓글 입력 도착")
    print(data)
    result = {}
    result["resultDB"] = boardService.insertComment(data)
    return result

@app.route('/board/comment/del', methods=['POST'])
def delComment():
    data={}
    data = request.get_json()
    print("댓글 입력 도착")
    print(data)
    result = {}
    result["resultDB"] = boardService.delComment(data)
    return result