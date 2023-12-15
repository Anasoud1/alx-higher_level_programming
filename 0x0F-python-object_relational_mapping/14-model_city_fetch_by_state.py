#!/usr/bin/python3
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
for instance in session.query(State.name, City.id, City.name).filter(
                State.id == City.state_id):
    print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))

session.close()
