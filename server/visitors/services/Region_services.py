from models.Region import Region
from repository.RegionRepository import RegionRepository
from dto.Region_DTO import RegionDTO
from exceptions.exceptions import ItemNotFoundException

class RegionServices:
    def __init__(self):
        self.repo = RegionRepository()

    def add_region(self, dto: RegionDTO):
        region = Region(**dto.dict())
        self.repo.add(region)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        region = self.repo.get_by_id(id)
        if not region:
            raise ItemNotFoundException(id)
        return region

    def update(self, id, dto: RegionDTO):
        updated = Region(**dto.dict())
        result = self.repo.update(id, updated)
        if not result:
            raise ItemNotFoundException(id)
        return result

    def delete(self, id):
        result = self.repo.delete(id)
        if not result:
            raise ItemNotFoundException(id)
