from http import HTTPStatus

from fastapi import Depends, HTTPException
from typing import Optional

from plant.repository import PlantRepository, get_plant_repository
from plant.schema import PlantCreate, PlantUpdate, PlantRead, PlantPage, PlantReadWithComments
from util.decorators import with_error_logger


class PlantService:
    def __init__(self, repo: Depends(get_plant_repository)) -> None:
        self.plant_repository = repo

    @with_error_logger
    def get_by_id(self, plant_id: int):
        db_plant = self.plant_repository.get_by_id(plant_id)

        if db_plant is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                                detail=f"Plant with id: {plant_id} not found")

        return PlantReadWithComments.from_orm(db_plant)

    @with_error_logger
    def fetch(self,
              page_size: int,
              page: int,
              search_query: Optional[str] = None,
              sort_by: Optional[str] = None,
              sort_direction: Optional[str] = None):
        db_page = self.plant_repository.fetch(
            page_size, page, search_query, sort_by, sort_direction)
        return PlantPage.from_orm(db_page)

    @with_error_logger
    def create(self, entity: PlantCreate):
        db_plant = self.plant_repository.create(entity)
        return PlantRead.from_orm(db_plant)

    @with_error_logger
    def replacement_update(self,
                           plant_id: int,
                           plant_update: PlantUpdate):
        db_plant = self.plant_repository.update(plant_id, plant_update)

        if db_plant is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                                detail=f"Plant with id: {plant_id} not found")

        return PlantRead.from_orm(db_plant)

    @with_error_logger
    def patch_update(self,
                     plant_id: int,
                     plant_update: PlantUpdate):
        db_plant = self.plant_repository.get_by_id(plant_id)

        if db_plant is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                                detail=f"Plant with id: {plant_id} not found")

        for field, value in plant_update.dict(exclude_unset=True).items():
            setattr(db_plant, field, value)

        db_plant = self.plant_repository.update(plant_id, db_plant)

        return PlantRead.from_orm(db_plant)

    @with_error_logger
    def delete(self, item_id: int):
        db_plant = self.plant_repository.delete(item_id)
        return PlantRead.from_orm(db_plant)


def get_plant_service(repo: PlantRepository = Depends(get_plant_repository)):
    return PlantService(repo)
