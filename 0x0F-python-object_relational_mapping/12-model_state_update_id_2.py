#!/usr/bin/python3
""" Script that changes the name of a State object from a database """

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    s = Session(engine)
    r = s.query(State).filter(State.id == 2).first()
    r.name = 'New Mexico'
    s.commit()
    s.close()
