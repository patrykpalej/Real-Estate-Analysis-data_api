from sqlalchemy import Column, Integer, String, DateTime, Float

from db.orm import Base


class OtodomLands(Base):
    __tablename__ = "otodom_lands"

    number_id = Column("number_id", Integer, primary_key=True)
    url = Column("url", String)
    title = Column("title", String)
    price = Column("price", Integer)
    advertiser_type = Column("advertiser_type", String)
    utc_created_at = Column("utc_created_at", DateTime)
    province = Column("province", String)
    city = Column("city", String)
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
    land_area = Column("land_area", Integer)
