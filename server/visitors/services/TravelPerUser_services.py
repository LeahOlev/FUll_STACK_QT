from models.TravelPerUser import TravelPerUser
from repository.TravelPerUserRepository import TravelPerUserRepository
from dto.TravelPerUser_DTO import TravelPerUserDTO
from exceptions.exceptions import ItemNotFoundException

class TravelPerUserServices:
    def __init__(self, repo=None):
        self.repo = repo or TravelPerUserRepository()

    def add(self, dto: TravelPerUserDTO):
        item = TravelPerUser(**dto.dict())
        self.repo.add(item)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        item = self.repo.get_by_id(id)
        if not item:
            raise ItemNotFoundException(id)
        return item

    def update(self, id, dto: TravelPerUserDTO):
        updated = TravelPerUser(**dto.dict())
        result = self.repo.update(id, updated)
        if not result:
            raise ItemNotFoundException(id)
        return result

    def delete(self, id):
        result = self.repo.delete(id)
        if not result:
            raise ItemNotFoundException(id)
