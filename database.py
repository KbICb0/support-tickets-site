from sqlalchemy import create_engine
from models import Base

engine = create_engine("sqlite:///./support_tickets_sqlite.db", echo=True)

print(engine)

def create_db_and_tables():
    Base.metadata.create_all(engine)

create_db_and_tables()