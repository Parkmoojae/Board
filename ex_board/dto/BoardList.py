from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN
from dataSource import Base

__all__ = ['BoardList']

class BoardList(Base):
    __tablename__ = "board_list"
    __table_args__ = {
                        'comment' : '게시판 정보'
    }

    BOARD_ID                             = Column(VARCHAR(50), primary_key=True, comment='게시판 고유 식별 번호')
    BOARD_NAME                           = Column(VARCHAR(50), nullable=False, comment='게시판 이름')
    BOARD_DES                            = Column(VARCHAR(50), nullable=False, comment='게시판 설명')
    
    def __init__(self, boardId, **kwargs):
        self.BOARD_ID = boardId

        self.BOARD_NAME                    = kwargs.get('BOARD_NAME', None)
        self.BOARD_DES                     = kwargs.get('BOARD_DES', None)

    def __repr__(self):
        return "{'BOARD_ID' : '%s', \
        'BOARD_NAME' : '%s', \
        'BOARD_DES' : '%s'}" % (
                    self.BOARD_ID,
                    self.BOARD_NAME,
                    self.BOARD_DES)