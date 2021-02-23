from dataSource import *
from sqlalchemy import text, exc, and_, or_, func, String, DateTime, Integer, Sequence
from sqlalchemy.sql import bindparam
from commonUtil import *
from dto import *
import uuid, datetime

def postList(boardId, pageNum):
    # query = """
    # with recursive cte as
    # (
    # select     board_common_id,
    #             board_id,
    #             board_common_title,
    #             board_common_no,
    #             board_common_pno,
    #             user_no

    #             0 AS depth,
    #             CAST(board_common_no AS VARCHAR(1000)) as lvl,
    #             CAST(LPAD(board_common_no, 10, "0") AS VARCHAR(1000)) as lvl2
    # from       board_common
    # where      board_id = 101 AND board_common_pno = 0
    # union all
    # select     r.board_common_id,
    #                 r.board_id,
    #                 r.board_common_title,
    #             r.board_common_no,
    #             r.board_common_pno,
    #             r.user_no,

    #             1 + depth AS depth,
    #             CONCAT(cte.lvl, "-", r.board_common_no) as lvl,
    #             CONCAT(cte.lvl2, "-", LPAD(r.board_common_no, 10, "0")) as lvl2
    # from       board_common r

    # inner join cte
    #         on r.board_common_pno = cte.board_common_no

    # WHERE		r.board_id = 101
    # )
    # select ct.board_common_id, ct.board_id, ct.board_common_title, ct.board_common_no, ct.board_common_pno, ct.lvl1, ct.lvl2, ct.depth, us.user_id 
    # from (select * from cte
    # ORDER BY lvl2) as ct
    # left join user as us
    # on ct.user_no = us.user_no;
    # """

     # query = """
    #         with recursive cte as
    #         (
    #         select 
 	# 		    board_id,
 	# 			board_common_title,
    #             board_common_no,
    #             board_common_pno,
    #             user_no,
    #             board_common_regdate,
    #             board_common_modidate,
    #             board_common_count,
    #             board_common_del,
            
    #                     0 AS depth,
    #                     CAST(board_common_no AS VARCHAR(1000)) as lvl,
    #                     CAST(LPAD(board_common_no, 10, "0") AS VARCHAR(1000)) as lvl2
    #         from       board_common
    #         where      board_id = :boardId AND board_common_pno = 0
    #         union all
    #         select   
    #             r.board_id,
    #             r.board_common_title,
    #             r.board_common_no,
    #             r.board_common_pno,
    #             r.user_no,
    #             r.board_common_regdate,
    #             r.board_common_modidate,
    #             r.board_common_count,
    #             r.board_common_del,
            
    #                 1 + depth AS depth,
    #                 CONCAT(cte.lvl, "-", r.board_common_no) as lvl,
    #                 CONCAT(cte.lvl2, "-", LPAD(r.board_common_no, 10, "0")) as lvl2
    #         from       board_common r

    #         inner join cte
    #             on r.board_common_pno = cte.board_common_no

    #         WHERE		r.board_id = :boardId
	#         )
	#         SELECT 
	# 		     t.board_id, 
	# 		    t.board_common_title, 
	# 		    t.board_common_no, 
	# 		    t.board_common_pno, 
	# 		    t.user_no, 
	# 		    t.depth, 
	# 		    t.lvl, 
    #             t.lvl2,
    #             t.board_common_regdate,
    #             t.board_common_modidate,
    #             t.board_common_count,
    #             t.board_common_del, 
    #             u.user_id,
    #             bl.board_name,
    #             @ROWNUM := @ROWNUM + 1 AS ROWNUM

	#         FROM
    #         (SELECT @ROWNUM := 0 ) R,
    #         (SELECT * FROM cte) AS t
	#         LEFT JOIN user AS u
	#         ON t.user_no = u.user_no
    #         LEFT JOIN board_list AS bl
    #         ON t.board_id = bl.board_id
    #      	ORDER BY t.lvl2;
    #     """

    query = """
            with recursive cte as
            (
            select     
 			    board_id,
 				board_common_title,
                board_common_no,
                board_common_pno,
                user_no,
                board_common_regdate,
                board_common_modidate,
                board_common_count,
                board_common_del,
            
                        0 AS depth,
                        CAST(board_common_no AS VARCHAR(1000)) as lvl,
                        CAST(LPAD(board_common_no, 10, "0") AS VARCHAR(1000)) as lvl2
            from       board_common
            where      board_id = :boardId AND board_common_pno = 0
            union all
            select    
                r.board_id,
                r.board_common_title,
                r.board_common_no,
                r.board_common_pno,
                r.user_no,
                r.board_common_regdate,
                r.board_common_modidate,
                r.board_common_count,
                r.board_common_del,
            
                    1 + depth AS depth,
                    CONCAT(cte.lvl) as lvl,
                    CONCAT(cte.lvl2, "-", LPAD(r.board_common_no, 10, "0")) as lvl2
            from       board_common r

            inner join cte
                on r.board_common_pno = cte.board_common_no

            WHERE		r.board_id = :boardId
	        )
	        SELECT *
	        FROM
	        (
	        SELECT cte3.*, @ROWNUM := @ROWNUM + 1  AS total_num
	        FROM(
	        SELECT cte2.*, rank() over(ORDER BY cte2.lvl) AS ROWNUM
	        FROM
			  (SELECT 
				t.board_common_no,
				t.board_common_pno,
				t.depth, 
			    t.lvl, 
                t.lvl2,
			     t.board_id, 
			    t.board_common_title, 
			    t.user_no, 
                t.board_common_regdate,
                t.board_common_modidate,
                t.board_common_count,
                t.board_common_del, 
                u.user_id,
                bl.board_name

	        FROM
            (SELECT * FROM cte) AS t
	        LEFT JOIN user AS u
	        ON t.user_no = u.user_no
            LEFT JOIN board_list AS bl
            ON t.board_id = bl.board_id
            ORDER BY t.lvl2 DESC)cte2)cte3,
            (SELECT @ROWNUM := 0 ) R) cte4
            WHERE 10*(:pageNum-1)<total_num AND (10*:pageNum)+1>total_num;
        """

   

    stmt = text(query)
    stmt = stmt.bindparams(bindparam("boardId", type_=Integer), bindparam("pageNum", type_=Integer))
    result = session.execute(stmt, {"boardId": int(boardId), "pageNum": int(pageNum)})
    # result = session.execute(stmt, {"ID": data["ID"], "now": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') , "userId":data["userId"], "userName":data["userName"]})

    print("@@@@@@@@@@@@@@@@")
    print(type(result))
    print(result)
    print("@@@@@@@@@@@@@@@@")

    # result 값을 [key: value]의 list 형태로 변경
    # resultVal = [{column: value for column, value in rowproxy.items() }for rowproxy in result]
    resultVal = resultToDict(result)
    print(resultVal)
    print(type(resultVal))

    return resultVal


def boardList():
    queryResult = session.query(BoardList).with_entities(BoardList.BOARD_ID, BoardList.BOARD_NAME, BoardList.BOARD_DES)

    resultVal = queryToDict(queryResult)

    print(resultVal)
    print(type(resultVal))
    
    return resultVal

from dto import *
def getContent(boardCommonNo):

    # temp = session.query(BoardCommon, BoardList).join(BoardCommon, BoardCommon.BOARD_COMMON_ID == BoardList.BOARD_ID)

    # queryResult = temp.with_entities(BoardCommon.BOARD_COMMON_CONTENT, BoardCommon.BOARD_COMMON_TITLE, BoardList.BOARD_NAME).\
    #                 filter(BoardCommon.BOARD_COMMON_ID == boardCommonId)

    # qeuryResult = session.query(BoardCommon).with_entities(BoardCommon.BOARD_COMMON_CONTENT, BoardCommon.BOARD_COMMON_TITLE).\
    #                 filter(BoardCommon.BOARD_COMMON_ID == boardCommonId)

    queryResult = session.query(BoardCommon, User).\
                    with_entities(BoardCommon.USER_NO, BoardCommon.BOARD_COMMON_CONTENT, BoardCommon.BOARD_COMMON_TITLE, BoardCommon.BOARD_COMMON_DEL, BoardCommon.BOARD_COMMON_REGDATE, BoardCommon.BOARD_COMMON_MODIDATE, BoardCommon.BOARD_COMMON_NO, BoardCommon.BOARD_COMMON_PNO, BoardCommon.BOARD_ID, BoardCommon.BOARD_COMMON_COUNT, User.USER_ID).\
                    filter(BoardCommon.USER_NO == User.USER_NO).\
                    filter(BoardCommon.BOARD_COMMON_NO==boardCommonNo)
    

    resultVal = queryToDict(queryResult)
    print("@@@@@@@ Content @@@@@@@")
    print(type(resultVal))
    print(resultVal)
    return resultVal

    
def insertContent(data):
    boardCommon = BoardCommon(  BOARD_ID = data['boardId'], 
                                USER_NO = data['userNo'], 
                                BOARD_COMMON_TITLE = data['boardCommonTitle'], 
                                BOARD_COMMON_CONTENT = data['boardCommonContent'],
                                BOARD_COMMON_REGDATE = nowTime(),
                                BOARD_COMMON_COUNT = 1,
                                BOARD_COMMON_DEL = False,
                                BOARD_COMMON_PNO = data['boardCommonPno']
                                )
    try:
        session.add(boardCommon)
        session.commit()
        resultCode = '200'
    except:
        session.rollback()
        resultCode = '500'
        raise
    finally:
        session.close()  # optional, depends on use case


    print("########")
    print(resultCode)
    print("########")
    
    return resultCode



def updateContent(data):

    resultCode = -1
    # queryOptions = ['URI', 'NAME', 'PARENT_ID', 'TYPE', 'ICON', 'STATUS', 'CATEGORY', 'DESCRIPTION', 'IMAGE']
    updateContent = {}
    updateContent['BOARD_COMMON_MODIDATE'] = nowTime()
    updateContent['BOARD_COMMON_TITLE'] = data['boardCommonTitle']
    updateContent['BOARD_COMMON_CONTENT'] = data['boardCommonContent']

    # for queryOption in queryOptions:
    #     if data.get(queryOption, None) is not None:
    #         updateContent[queryOption] = data[queryOption]

    result = session.query(BoardCommon).\
        filter(and_(
            (BoardCommon.BOARD_COMMON_NO == data['boardCommonNo']),
            (BoardCommon.BOARD_ID == data['boardId'])
            )).\
        update(updateContent, synchronize_session='fetch')
        
    session.commit()
    
    if result==1:
        resultCode = '200'
    else:
        resultCode = '500'
    return resultCode



def getBoardToModi(boardCommonNo):
    queryResult = session.query(BoardCommon, User).\
                    with_entities(BoardCommon.USER_NO, BoardCommon.BOARD_COMMON_CONTENT, BoardCommon.BOARD_COMMON_TITLE, BoardCommon.BOARD_COMMON_DEL, BoardCommon.BOARD_COMMON_REGDATE, BoardCommon.BOARD_COMMON_MODIDATE, BoardCommon.BOARD_COMMON_NO, BoardCommon.BOARD_COMMON_PNO, BoardCommon.BOARD_ID, BoardCommon.BOARD_COMMON_COUNT, User.USER_ID).\
                    filter(BoardCommon.USER_NO == User.USER_NO).\
                    filter(BoardCommon.BOARD_COMMON_NO==boardCommonNo)
    

    resultVal = queryToDict(queryResult)
    print("@@@@@@@ modiContent @@@@@@@")
    print(type(resultVal))
    print(resultVal)

    return resultVal


def deletePost(data):
    resultCode = -1
    # queryOptions = ['URI', 'NAME', 'PARENT_ID', 'TYPE', 'ICON', 'STATUS', 'CATEGORY', 'DESCRIPTION', 'IMAGE']
    updateContent = {}
    updateContent['BOARD_COMMON_DELDATE'] = nowTime()
    updateContent['BOARD_COMMON_DEL'] = 1

    # for queryOption in queryOptions:
    #     if data.get(queryOption, None) is not None:
    #         updateContent[queryOption] = data[queryOption]

    result = session.query(BoardCommon).\
        filter(and_(
            (BoardCommon.BOARD_COMMON_NO == data['boardCommonNo']),
            (BoardCommon.BOARD_ID == data['boardId'])
            )).\
        update(updateContent, synchronize_session='fetch')
        
    session.commit()
    
    if result==1:
        resultCode = '200'
    else:
        resultCode = '500'
    return resultCode
    
    # resultCode = '-1'
    # result = session.query(BoardCommon).\
    #     filter(BoardCommon.BOARD_COMMON_NO==data['boardCommonNo']).\
    #     delete()
    # session.commit()

    # if result>=1:
    #     resultCode=200
    # else:
    #     resultCode=500
    # return resultCode



def getReply(boardCommonNo):
    query = """
            with recursive cte as
            (
             select     board_common_no,
 			        	board_comment_id,
 				        board_comment_pid,
 				        board_comment_content,
                        board_comment_regdate,
                        board_comment_modidate,
                        user_no,
                        board_comment_del,
                        board_comment_deldate,
            
                        0 AS depth,
                        CAST(board_comment_id AS VARCHAR(1000)) as lvl,
                        CAST(LPAD(board_comment_id, 10, "0") AS VARCHAR(1000)) as lvl2
            from       board_comment
            where      board_common_no = :boardCommonNo AND board_comment_pid = 0
            union all
            SELECT     r.board_common_no,
                        r.board_comment_id,
                        r.board_comment_pid,
                        r.board_comment_content,
                        r.board_comment_regdate,
                        r.board_comment_modidate,
                        r.user_no,
                        r.board_comment_del,
                        r.board_comment_deldate,
                        
                        1 + depth AS depth,
                        CONCAT(cte.lvl, "-", r.board_comment_id) as lvl,
                        CONCAT(cte.lvl2, "-", LPAD(r.board_comment_id, 10, "0")) as lvl2
            from       board_comment r

             inner join cte
            on r.board_comment_pid = cte.board_comment_id

            WHERE		r.board_common_no = :boardCommonNo
	        )       
            SELECT c.*, u.user_id FROM cte c
            LEFT JOIN user AS u
            ON c.user_no = u.user_no
            ORDER BY lvl2;
        """

    stmt = text(query)
    stmt = stmt.bindparams(bindparam("boardCommonNo", type_=Integer))
    result = session.execute(stmt, {"boardCommonNo": int(boardCommonNo)})
    # result = session.execute(stmt, {"ID": data["ID"], "now": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') , "userId":data["userId"], "userName":data["userName"]})

    print("@@@@@getReply@@@@@")
    print(type(result))
    print(result)
    print("@@@@@@@@@@@@@@@@")

    # result 값을 [key: value]의 list 형태로 변경
    # resultVal = [{column: value for column, value in rowproxy.items() }for rowproxy in result]
    resultVal = resultToDict(result)
    print(resultVal)
    print(type(resultVal))

    return resultVal



# 댓글 입력
def insertComment(data):
    print(data)
    boardComment = BoardComment(  BOARD_COMMON_NO = data['boardCommonNo'], 
                                USER_NO = data['userNo'], 
                                BOARD_COMMENT_CONTENT = data['boardCommentContent'], 
                                BOARD_COMMENT_REGDATE = nowTime(),
                                BOARD_COMMENT_DEL = False,
                                BOARD_COMMENT_PID = int(data['boardCommentPid'])
                                )
    try:
        session.add(boardComment)
        session.commit()
        resultCode = '200'
    except:
        session.rollback()
        resultCode = '500'
        raise
    finally:
        session.close()  # optional, depends on use case


    print("########")
    print(resultCode)
    print("########")
    
    return resultCode

def delComment(data):
    resultCode = -1
    # queryOptions = ['URI', 'NAME', 'PARENT_ID', 'TYPE', 'ICON', 'STATUS', 'CATEGORY', 'DESCRIPTION', 'IMAGE']
    updateContent = {}
    updateContent['BOARD_COMMENT_DELDATE'] = nowTime()
    updateContent['BOARD_COMMENT_DEL'] = 1

    # for queryOption in queryOptions:
    #     if data.get(queryOption, None) is not None:
    #         updateContent[queryOption] = data[queryOption]

    result = session.query(BoardComment).\
        filter(and_(
            (BoardComment.BOARD_COMMENT_ID == data['boardCommentId']),
            (BoardComment.BOARD_COMMON_NO == data['boardCommonNo'])
            )).\
        update(updateContent, synchronize_session='fetch')
        
    session.commit()
    
    if result==1:
        resultCode = '200'
    else:
        resultCode = '500'
    return resultCode




def totalPage(boardId):
    queryResult = session.query(BoardCommon).\
                    with_entities(BoardCommon.BOARD_COMMON_NO).\
                    filter(BoardCommon.BOARD_ID==boardId)
    
    print(len(queryResult.all()))

    return len(queryResult.all())