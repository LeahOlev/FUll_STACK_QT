from models.Users import Users
from repository.UserRepository import UserRepository
from dto.User_DTO import UserDTO
from exceptions.exceptions import ItemNotFoundException, ItemAlreadyExistsException

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def add_user(self, dto: UserDTO):
        if self.repo.get_by_id(dto.id):
            raise ItemAlreadyExistsException(dto.id)
        user = Users(id=dto.id, name=dto.name, email=dto.email)
        self.repo.add(user)

    def get_all_users(self):
        return self.repo.get_all()

    def get_user_by_id(self, user_id):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ItemNotFoundException(user_id)
        return user

    def update_user(self, user_id, dto: UserDTO):
        updated_user = Users(id=dto.id, name=dto.name, email=dto.email)
        result = self.repo.update(user_id, updated_user)
        if not result:
            raise ItemNotFoundException(user_id)
        return result

    def delete_user(self, user_id):
        user = self.repo.delete(user_id)
        if not user:
            raise ItemNotFoundException(user_id)
