from db.models.domiporta.houses import DomiportaHouses


def filter_houses(query, min_price, max_price, min_area, max_area, min_m2_price,
                  max_m2_price, min_build_year, max_build_year, province, city):
    if min_price is not None:
        query = query.filter(DomiportaHouses.price >= min_price)
    if max_price is not None:
        query = query.filter(DomiportaHouses.price <= max_price)
    if min_area is not None:
        query = query.filter(DomiportaHouses.house_area >= min_area)
    if max_area is not None:
        query = query.filter(DomiportaHouses.house_area <= max_area)
    if min_m2_price is not None:
        query = query.filter(DomiportaHouses.price / DomiportaHouses.house_area >= min_m2_price)
    if max_m2_price is not None:
        query = query.filter(DomiportaHouses.price / DomiportaHouses.house_area <= max_m2_price)
    if min_build_year is not None:
        query = query.filter(DomiportaHouses.build_year >= min_build_year)
    if max_build_year is not None:
        query = query.filter(DomiportaHouses.build_year <= max_build_year)
    if province is not None:
        query = query.filter(DomiportaHouses.province == province)
    if city is not None:
        query = query.filter(DomiportaHouses.city == city)
    
    return query
