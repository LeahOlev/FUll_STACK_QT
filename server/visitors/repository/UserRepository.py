from config import Session
from models.Users import Users
from sqlalchemy.orm import Session


class UserRepository:

    def add(self, users):
        session = Session()
        try:
            session.add(users)
            session.commit()
        finally:
            session.close()

    def get_all(self):
        session = Session()
        try:
            return session.query(Users).all()
        finally:
            session.close()

    def get_by_id(self, id):
        session = Session()
        try:
            return session.query(Users).filter_by(id=id).first()
        finally:
            session.close()

    def update(self, UserID, new_data: Users):
        session=Session()
        UserID = self.get_by_id(UserID)
        if UserID:
            UserID.UserID =new_data.UserID
            UserID.FirstName=new_data.FirstName
            UserID.Lastname = new_data.LastName
            UserID.Email =new_data.Email
            session.commit()
        return UserID


    def delete(self, id):
        session = Session()
        try:
            user = session.query(Users).filter_by(id=id).first()
            if user:
                session.delete(user)
                session.commit()
            return user
        finally:
            session.close()

    def exists_by_name(self, FirstName):
        session = Session()
        return session.query(Users).filter_by(FirstName=FirstName).first() is not None
