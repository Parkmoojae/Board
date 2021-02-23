from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN, Table, Sequence, String, ForeignKey
from dataSource import Base, metadata

def _create_hobby_table():
    hobby = Table('hobby', metadata,
                  Column('hobby_id', Integer, Sequence('hobby_id_seq'),
                         primary_key=True),
                  )

    # addresses = Table('addresses', metadata,
    #                   Column('id', Integer, Sequence('address_id_seq'),
    #                          primary_key=True),
    #                   Column('user_id', None, ForeignKey('users.id')),
    #                   Column('email_address', String, nullable=False)
    #                   )
    metadata.create_all(Base)
    return hobby