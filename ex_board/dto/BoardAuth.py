from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN, NUMERIC
from dataSource import Base

__all__ = ['BoardAuth']

class BoardAuth(Base):
    __tablename__ = "board_auth"
    __table_args__ = {
                        'comment' : '게시판 공통'
    }

    BOARD_COMMON_NO                      = Column(Integer, primary_key=True, autoincrement=True, comment='게시글 고유 식별 번호')
    BOARD_ID                             = Column(VARCHAR(50), nullable=False, comment='게시판 고유 식별 번호')
    USER_NO                              = Column(VARCHAR(255), comment='사용자 고유 식별 번호')
    BOARD_COMMON_TITLE                   = Column(VARCHAR(50), comment='게시글 제목')
    BOARD_COMMON_CONTENT                 = Column(VARCHAR(50), comment='게시글 내용')
    BOARD_COMMON_REGDATE                 = Column(DATETIME, comment='게시글 등록일')
    BOARD_COMMON_MODIDATE                = Column(DATETIME, comment='게시글 수정일')
    BOARD_COMMON_COUNT                   = Column(NUMERIC(11), comment='게시글 조회수')
    BOARD_COMMON_DEL                     = Column(BOOLEAN, comment='게시글 삭제 상태')
    BOARD_COMMON_DELDATE                 = Column(DATETIME, comment='게시글 삭제일')
    BOARD_COMMON_PNO                     = Column(NUMERIC(11), comment='게시글 부모번호')
    
    def __init__(self, **kwargs):

        self.BOARD_ID                      = kwargs.get('BOARD_ID', None)
        self.USER_NO                       = kwargs.get('USER_NO', None)
        self.BOARD_COMMON_TITLE            = kwargs.get('BOARD_COMMON_TITLE', None)
        self.BOARD_COMMON_CONTENT          = kwargs.get('BOARD_COMMON_CONTENT', None)
        self.BOARD_COMMON_REGDATE          = kwargs.get('BOARD_COMMON_REGDATE', None)
        self.BOARD_COMMON_MODIDATE         = kwargs.get('BOARD_COMMON_MODIDATE', None)
        self.BOARD_COMMON_COUNT            = kwargs.get('BOARD_COMMON_COUNT', None)
        self.BOARD_COMMON_DEL              = kwargs.get('BOARD_COMMON_DEL', None)
        self.BOARD_COMMON_DELDATE          = kwargs.get('BOARD_COMMON_DELDATE', None)
        self.BOARD_COMMON_NO               = kwargs.get('BOARD_COMMON_NO', None)
        self.BOARD_COMMON_PNO              = kwargs.get('BOARD_COMMON_PNO', None)

    def __repr__(self):
        return "{'BOARD_COMMON_NO' : '%s', \
        'BOARD_ID' : '%s', \
        'USER_NO' : '%s', \
        'BOARD_COMMON_TITLE' : '%s', \
        'BOARD_COMMON_CONTENT' : '%s', \
        'BOARD_COMMON_REGDATE' : '%s', \
        'BOARD_COMMON_MODIDATE' : '%s', \
        'BOARD_COMMON_COUNT' : '%s', \
        'BOARD_COMMON_DEL' : '%s', \
        'BOARD_COMMON_DELDATE' : '%s', \
        'BOARD_COMMON_PNO' : '%s'}" % (
                    self.BOARD_COMMON_NO,
                    self.BOARD_ID,
                    self.USER_NO,
                    self.BOARD_COMMON_TITLE,
                    self.BOARD_COMMON_CONTENT,
                    self.BOARD_COMMON_REGDATE,
                    self.BOARD_COMMON_MODIDATE,
                    self.BOARD_COMMON_COUNT,
                    self.BOARD_COMMON_DEL,
                    self.BOARD_COMMON_DELDATE,
                    self.BOARD_COMMON_PNO)