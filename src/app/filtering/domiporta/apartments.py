from db.models.domiporta.apartments import DomiportaApartments


def filter_apartments(query, min_price, max_price, min_area, max_area, min_m2_price, max_m2_price,
                      min_build_year, max_build_year, province, city):
    if min_price is not None:
        query = query.filter(DomiportaApartments.price >= min_price)
    if max_price is not None:
        query = query.filter(DomiportaApartments.price <= max_price)
    if min_area is not None:
        query = query.filter(DomiportaApartments.apartment_area >= min_area)
    if max_area is not None:
        query = query.filter(DomiportaApartments.apartment_area <= max_area)
    if min_m2_price is not None:
        query = query.filter(DomiportaApartments.price / DomiportaApartments.apartment_area >= min_m2_price)
    if max_m2_price is not None:
        query = query.filter(DomiportaApartments.price / DomiportaApartments.apartment_area <= max_m2_price)
    if min_build_year is not None:
        query = query.filter(DomiportaApartments.build_year >= min_build_year)
    if max_build_year is not None:
        query = query.filter(DomiportaApartments.build_year <= max_build_year)
    if province is not None:
        query = query.filter(DomiportaApartments.province == province)
    if city is not None:
        query = query.filter(DomiportaApartments.city == city)
    
    return query
