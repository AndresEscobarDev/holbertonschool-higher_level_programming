#!/usr/bin/python3
""" Script that lists all State objects that
contain the letter a from a database """

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
    r = s.query(State).filter(State.name == sys.argv[4]).first()
    if r:
        print(r.id)
    else:
        print("Not found")
    s.close()
