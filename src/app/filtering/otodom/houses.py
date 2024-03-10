from db.models.otodom.houses import OtodomHouses


def filter_houses(query, min_price, max_price, min_area, max_area, min_m2_price,
                  max_m2_price, min_lot_area, max_lot_area, min_build_year, max_build_year,
                  min_offer_date, max_offer_date, advertiser, province, city, market):
    if min_price is not None:
        query = query.filter(OtodomHouses.price >= min_price)
    if max_price is not None:
        query = query.filter(OtodomHouses.price <= max_price)
    if min_area is not None:
        query = query.filter(OtodomHouses.house_area >= min_area)
    if max_area is not None:
        query = query.filter(OtodomHouses.house_area <= max_area)
    if min_m2_price is not None:
        query = query.filter(OtodomHouses.price / OtodomHouses.house_area >= min_m2_price)
    if max_m2_price is not None:
        query = query.filter(OtodomHouses.price / OtodomHouses.house_area <= max_m2_price)
    if min_lot_area is not None:
        query = query.filter(OtodomHouses.lot_area >= min_lot_area)
    if max_lot_area is not None:
        query = query.filter(OtodomHouses.lot_area <= max_lot_area)
    if min_build_year is not None:
        query = query.filter(OtodomHouses.build_year >= min_build_year)
    if max_build_year is not None:
        query = query.filter(OtodomHouses.build_year <= max_build_year)
    if min_offer_date is not None:
        query = query.filter(OtodomHouses.utc_created_at >= min_offer_date)
    if max_offer_date is not None:
        query = query.filter(OtodomHouses.utc_created_at <= max_offer_date)
    if advertiser is not None:
        query = query.filter(OtodomHouses.advertiser_type == advertiser)
    if province is not None:
        query = query.filter(OtodomHouses.province == province)
    if city is not None:
        query = query.filter(OtodomHouses.city == city)
    if market is not None:
        query = query.filter(OtodomHouses.market == market)

    return query
