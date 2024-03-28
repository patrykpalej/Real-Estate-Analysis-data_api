from db.models.otodom.apartments import OtodomApartments


def filter_apartments(query, min_price, max_price, min_area, max_area, min_m2_price, max_m2_price,
                      min_build_year, max_build_year, min_offer_date, max_offer_date,
                      advertiser, province, city, market):
    if min_price is not None:
        query = query.filter(OtodomApartments.price >= min_price)
    if max_price is not None:
        query = query.filter(OtodomApartments.price <= max_price)
    if min_area is not None:
        query = query.filter(OtodomApartments.apartment_area >= min_area)
    if max_area is not None:
        query = query.filter(OtodomApartments.apartment_area <= max_area)
    if min_m2_price is not None:
        query = query.filter(OtodomApartments.price / OtodomApartments.apartment_area >= min_m2_price)
    if max_m2_price is not None:
        query = query.filter(OtodomApartments.price / OtodomApartments.apartment_area <= max_m2_price)
    if min_build_year is not None:
        query = query.filter(OtodomApartments.build_year >= min_build_year)
    if max_build_year is not None:
        query = query.filter(OtodomApartments.build_year <= max_build_year)
    if min_offer_date is not None:
        query = query.filter(OtodomApartments.utc_created_at >= min_offer_date)
    if max_offer_date is not None:
        query = query.filter(OtodomApartments.utc_created_at <= max_offer_date)
    if advertiser is not None:
        query = query.filter(OtodomApartments.advertiser_type == advertiser)
    if province is not None:
        query = query.filter(OtodomApartments.province == province)
    if city is not None:
        query = query.filter(OtodomApartments.city == city)
    if market is not None:
        query = query.filter(OtodomApartments.market == market)

    return query
