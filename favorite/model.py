from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Favorite(Base):
    __tablename__ = "user_favorites"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    plant = relationship("Plant", backref="favorited_by", cascade="delete")
    user = relationship("User", backref="favorite_plants")
