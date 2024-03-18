from sqlalchemy import Column, Integer, String, Float

from db.orm import Base


class DomiportaHouses(Base):
    __tablename__ = "domiporta_houses"

    number_id = Column("number_id", Integer, primary_key=True)
    url = Column("url", String)
    title = Column("title", String)
    price = Column("price", Integer)
    province = Column("province", String)
    city = Column("city", String)
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
    build_year = Column("build_year", Integer)
    house_area = Column("area", Float)
