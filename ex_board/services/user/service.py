from dataSource import *
from sqlalchemy import text, exc, and_, or_, func, String, DateTime
import uuid, datetime
from commonUtil import *
from dto import *

# from dto.User import *
def userInsert(data):
    print(data)
    userNo = str(uuid.uuid4())
    resultCode = '500'
    user = User(userNo,
                AUTH_TYPE = 0,
                USER_ID = data['userId'],
                USER_PW = data['userPw'],
                USER_EMAIL = data['userEmail'],
                USER_PHONE = data['userPhone'],
                USER_SEX = data['userSex'],
                USER_BDAY = data['userBirth'],
                USER_ADD = data['userAdd'],
                USER_REG = datetime.datetime.now(),
                USER_DELETE = 0
            )
    # user = User(str(uuid.uuid4()), 
    #             AUTH_TYPE = False,
    #             USER_ID = data['userId'], 
    #             USER_PW=data['userPw'], 
    #             USER_EMAIL=data['userEmail'],
    #             USER_PHONE = data['userPhone'], 
    #             USER_SEX=data['userSex'], 
    #             USER_BDAY=data['userBirth'],
    #             USER_ADD = data['userAdd'], 
    #             USER_REG=datetime.datetime.now(),
    #             USER_DELETE=False)
    # try:
    #     session.add(user)
    #     session.commit()
    #     resultCode = '200'
    # except exc.IntegrityError:
    #     resultCode = "500"

    try:
        session.add(user)
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


def userLogin(data):
    resultVal = '-1'
    queryResult = session.query(User).\
                    with_entities(
                        User.USER_ID, User.USER_NO, User.USER_PW, User.USER_ADD,
                        User.USER_BDAY, User.USER_DELETE, User.USER_EMAIL, User.USER_LASTLOGIN,
                        User.USER_MODI, User.USER_PHONE, User.USER_REG, User.USER_SEX, User.AUTH_TYPE).\
                    filter(User.USER_ID==data['userId'])
    
    # queryResult.all()
    # [('test', 'a6345e29-f739-43cf-b25a-ebbb2b055f28', '123', '서울특별시 노원구 상계동 412동', datetime.datetime(2021, 1, 22, 0, 0), False, 'heyj1@naver.com', None, None, '01093833409', datetime.datetime(2021, 1, 16, 20, 15, 22), 'male')]
    
    resultVal = queryToDict(queryResult.all())
    print(resultVal)
    print(type(resultVal))
    
    return resultVal

def userLastlogin(userNo):
    resultVal = '-1'
    queryResult = session.query(User).\
                    filter(User.USER_NO==userNo).\
                    update({'USER_LASTLOGIN' : datetime.datetime.now()}, synchronize_session='fetch')
    
    session.commit()

    if queryResult==1:
        resultVal = '200'
    else:
        resultVal = '500'

    return resultVal

