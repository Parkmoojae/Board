from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN
from dataSource import Base

__all__ = ['User']

class User(Base):
    __tablename__ = "user"
    __table_args__ = {
                        'comment' : '회원정보'
    }

    USER_NO                              = Column(VARCHAR(50), primary_key=True, comment='회원 고유번호')
    AUTH_TYPE                            = Column(BOOLEAN, nullable=False, comment='권한 등급 / 관리자 1, 일반 0')
    USER_ID                              = Column(VARCHAR(50), nullable=False, comment='회원 아이디')
    USER_PW                              = Column(VARCHAR(50), nullable=False, comment='회원 비밀번호')
    USER_EMAIL                           = Column(VARCHAR(50), nullable=False, comment='회원 이메일')
    USER_PHONE                           = Column(VARCHAR(11), nullable=False, comment='회원 전화번호')
    USER_SEX                             = Column(VARCHAR(10), nullable=False, comment='회원 성별')
    USER_BDAY                            = Column(DATETIME, nullable=False, comment='회원 생일')
    USER_ADD                             = Column(VARCHAR(255), nullable=False, comment='회원 주소')
    USER_LASTLOGIN                       = Column(DATETIME, comment='회원 최근 로그인일')
    USER_REG                             = Column(DATETIME, nullable=False, comment='회원 가입일')
    USER_MODI                            = Column(DATETIME, comment='회원 정보수정일')
    USER_DELETE                          = Column(BOOLEAN, nullable=False, comment='회원 정보삭제 / 삭제 1, 비삭제 0')
    
    def __init__(self, userNo, **kwargs):
        self.USER_NO = userNo

        self.AUTH_TYPE                     = kwargs.get('AUTH_TYPE', None)
        self.USER_ID                       = kwargs.get('USER_ID', None)
        self.USER_PW                       = kwargs.get('USER_PW', None)
        self.USER_EMAIL                    = kwargs.get('USER_EMAIL', None)
        self.USER_PHONE                    = kwargs.get('USER_PHONE', None)
        self.USER_SEX                      = kwargs.get('USER_SEX', None)
        self.USER_BDAY                     = kwargs.get('USER_BDAY', None)
        self.USER_ADD                      = kwargs.get('USER_ADD', None)
        self.USER_LASTLOGIN                = kwargs.get('USER_LASTLOGIN', None)
        self.USER_REG                      = kwargs.get('USER_REG', None)
        self.USER_MODI                     = kwargs.get('USER_MODI', None)
        self.USER_DELETE                   = kwargs.get('USER_DELETE', None)

    def __repr__(self):
        return "{'USER_NO' : '%s', \
        'AUTH_TYPE' : '%s', \
        'USER_ID' : '%s', \
        'USER_PW' : '%s', \
        'USER_EMAIL' : '%s', \
        'USER_PHONE' : '%s', \
        'USER_SEX' : '%s', \
        'USER_BDAY' : '%s', \
        'USER_ADD' : '%s', \
        'USER_LASTLOGIN' : '%s', \
        'USER_REG' : '%s', \
        'USER_MODI' : '%s', \
        'USER_DELETE' : '%s'}" % (
                    self.USER_NO,
                    self.AUTH_TYPE,
                    self.USER_ID,
                    self.USER_PW,
                    self.USER_EMAIL,
                    self.USER_PHONE,
                    self.USER_SEX,
                    self.USER_BDAY,
                    self.USER_ADD,
                    self.USER_LASTLOGIN,
                    self.USER_REG,
                    self.USER_MODI,
                    self.USER_DELETE)