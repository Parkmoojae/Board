from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN, NUMERIC
from dataSource import Base

__all__ = ['BoardComment']

class BoardComment(Base):
    __tablename__ = "board_comment"
    __table_args__ = {
                        'comment' : '게시판 공통'
    }

    BOARD_COMMENT_ID                     = Column(Integer, primary_key=True, autoincrement=True, comment='댓글 고유 식별 번호')
    BOARD_COMMON_NO                      = Column(Integer, nullable=False, comment='게시글 고유 식별 번호')
    USER_NO                              = Column(VARCHAR(255), comment='사용자 고유 식별 번호')
    BOARD_COMMENT_CONTENT                = Column(VARCHAR(100), comment='댓글 내용')
    BOARD_COMMENT_REGDATE                = Column(DATETIME, comment='댓글 등록일')
    BOARD_COMMENT_MODIDATE               = Column(DATETIME, comment='댓글 수정일')
    BOARD_COMMENT_DEL                    = Column(BOOLEAN, comment='댓글 삭제 상태')
    BOARD_COMMENT_DELDATE                = Column(DATETIME, comment='댓글 삭제일')
    BOARD_COMMENT_PID                    = Column(NUMERIC(11), comment='댓글 부모번호')
    
    def __init__(self, **kwargs):

        self.BOARD_COMMON_NO               = kwargs.get('BOARD_COMMON_NO', None)
        self.USER_NO                       = kwargs.get('USER_NO', None)
        self.BOARD_COMMENT_CONTENT          = kwargs.get('BOARD_COMMENT_CONTENT', None)
        self.BOARD_COMMENT_REGDATE         = kwargs.get('BOARD_COMMENT_REGDATE', None)
        self.BOARD_COMMENT_MODIDATE        = kwargs.get('BOARD_COMMENT_MODIDATE', None)
        self.BOARD_COMMENT_DEL             = kwargs.get('BOARD_COMMENT_DEL', None)
        self.BOARD_COMMENT_DELDATE         = kwargs.get('BOARD_COMMENT_DELDATE', None)
        self.BOARD_COMMENT_PID              = kwargs.get('BOARD_COMMENT_PID', None)
        
    def __repr__(self):
        return "{'BOARD_COMMENT_ID' : '%s', \
        'BOARD_COMMON_NO' : '%s', \
        'USER_NO' : '%s', \
        'BOARD_COMMENT_CONTENT' : '%s', \
        'BOARD_COMMENT_REGDATE' : '%s', \
        'BOARD_COMMENT_MODIDATE' : '%s', \
        'BOARD_COMMENT_DEL' : '%s', \
        'BOARD_COMMENT_DELDATE' : '%s', \
        'BOARD_COMMENT_PID' : '%s'}" % (
                    self.BOARD_COMMENT_ID,
                    self.BOARD_COMMON_NO,
                    self.USER_NO,
                    self.BOARD_COMMENT_CONTENT,
                    self.BOARD_COMMENT_REGDATE,
                    self.BOARD_COMMENT_MODIDATE,
                    self.BOARD_COMMENT_DEL,
                    self.BOARD_COMMENT_DELDATE,
                    self.BOARD_COMMENT_PID)