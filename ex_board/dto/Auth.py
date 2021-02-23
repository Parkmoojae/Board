from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN
from dataSource import Base

__all__ = ['Auth']

class Auth(Base):
    __tablename__ = "auth"
    __table_args__ = {
                        'comment' : '권한 정보'
    }

    AUTH_TYPE                            = Column(BOOLEAN, primary_key=True, comment='권한 등급 / 관리자 1, 일반 0')
    AUTH_DES                             = Column(VARCHAR(100), nullable=False, comment='권한 설명')

    def __init__(self, authType, **kwargs):
        self.AUTH_TYPE = authType

        self.AUTH_DES                      = kwargs.get('AUTH_DES', None)

    def __repr__(self):
        return "{'AUTH_TYPE' : '%s', \
        'AUTH_DES' : '%s'}" % (
                    self.AUTH_TYPE,
                    self.AUTH_DES)