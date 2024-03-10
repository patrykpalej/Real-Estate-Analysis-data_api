from db.models.otodom.lands import OtodomLands


def filter_lands(query, min_price, max_price, min_area, max_area, min_m2_price,
                 max_m2_price, min_offer_date, max_offer_date, advertiser, province, city):
    if min_price is not None:
        query = query.filter(OtodomLands.price >= min_price)
    if max_price is not None:
        query = query.filter(OtodomLands.price <= max_price)
    if min_area is not None:
        query = query.filter(OtodomLands.land_area >= min_area)
    if max_area is not None:
        query = query.filter(OtodomLands.land_area <= max_area)
    if min_m2_price is not None:
        query = query.filter(OtodomLands.price / OtodomLands.land_area >= min_m2_price)
    if max_m2_price is not None:
        query = query.filter(OtodomLands.price / OtodomLands.land_area <= max_m2_price)
    if min_offer_date is not None:
        query = query.filter(OtodomLands.utc_created_at >= min_offer_date)
    if max_offer_date is not None:
        query = query.filter(OtodomLands.utc_created_at <= max_offer_date)
    if advertiser is not None:
        query = query.filter(OtodomLands.advertiser_type == advertiser)
    if province is not None:
        query = query.filter(OtodomLands.province == province)
    if city is not None:
        query = query.filter(OtodomLands.city == city)

    return query
