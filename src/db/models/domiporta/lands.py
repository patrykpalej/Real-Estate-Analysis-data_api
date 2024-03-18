from sqlalchemy import Column, Integer, String, Float

from db.orm import Base


class DomiportaLands(Base):
    __tablename__ = "domiporta_lands"

    number_id = Column("number_id", Integer, primary_key=True)
    url = Column("url", String)
    title = Column("title", String)
    price = Column("price", Integer)
    province = Column("province", String)
    city = Column("city", String)
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
    land_area = Column("land_area", Integer)
