from sqlalchemy.orm import sessionmaker
from database import engine
from models import User




Session = sessionmaker(engine)

admin = User(name="admin", password="admin", email="testadmin@example.com", status="Online",roles="Administrator")
def create_user(user:User, session):
    session.add(user)

with Session() as session:
    try: 
        create_user(admin, session)
    except:
        session.rollback()
        raise
    else:
        session.commit