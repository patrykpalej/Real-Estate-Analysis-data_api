from db.models.domiporta.lands import DomiportaLands


def filter_lands(query, min_price, max_price, min_area, max_area, min_m2_price,
                 max_m2_price, province, city):
    if min_price is not None:
        query = query.filter(DomiportaLands.price >= min_price)
    if max_price is not None:
        query = query.filter(DomiportaLands.price <= max_price)
    if min_area is not None:
        query = query.filter(DomiportaLands.land_area >= min_area)
    if max_area is not None:
        query = query.filter(DomiportaLands.land_area <= max_area)
    if min_m2_price is not None:
        query = query.filter(DomiportaLands.price / DomiportaLands.land_area >= min_m2_price)
    if max_m2_price is not None:
        query = query.filter(DomiportaLands.price / DomiportaLands.land_area <= max_m2_price)
    if province is not None:
        query = query.filter(DomiportaLands.province == province)
    if city is not None:
        query = query.filter(DomiportaLands.city == city)

    return query
