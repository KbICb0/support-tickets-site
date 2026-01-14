from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from database import engine
from models import User, Ticket




Session = sessionmaker(engine)

admin = User(name="admin", password="admin", email="testadmin@example.com", roles="Administrator")
tiket = Ticket(name="test asign", status="Assigned", user_id=1, description="Test Assigment")
tiket2 = Ticket(name="test asign", status="Assigned", user_id=1, description="Test Assigment")
tiket3 = Ticket(name="test asign", status="Assigned", user_id=1, description="Test Assigment")

with Session.begin() as session:
    #session.add(admin)
    #session.add(tiket2)
    #session.add(tiket3)
    stmt = select(User)
    print(stmt)
    print(select(User.tickets))
with engine.connect() as conn:
    for row in conn.execute(stmt):
       print(row)
    user = session.query(User)
print(user)