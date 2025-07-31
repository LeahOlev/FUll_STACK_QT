from models.Visitors import Visitors
from repository.VisitorRepository import VisitorRepository
from dto.Visitor_DTO import VisitorDTO
from exceptions.exceptions import ItemNotFoundException

class VisitorServices:
    def __init__(self):
        self.repo = VisitorRepository()

    def add_visitor(self, dto: VisitorDTO):
        visitor = Visitors(**dto.dict())
        self.repo.add(visitor)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        visitor = self.repo.get_by_id(id)
        if not visitor:
            raise ItemNotFoundException(id)
        return visitor

    def update(self, id, dto: VisitorDTO):
        updated = Visitors(**dto.dict())
        result = self.repo.update(id, updated)
        if not result:
            raise ItemNotFoundException(id)
        return result

    def delete(self, id):
        result = self.repo.delete(id)
        if not result:
            raise ItemNotFoundException(id)
