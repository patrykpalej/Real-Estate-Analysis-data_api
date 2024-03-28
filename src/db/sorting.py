from db.models.otodom.apartments import OtodomApartments
from db.models.otodom.houses import OtodomHouses
from db.models.otodom.lands import OtodomLands
from db.models.domiporta.apartments import DomiportaApartments
from db.models.domiporta.houses import DomiportaHouses
from db.models.domiporta.lands import DomiportaLands


def sort_results(query, sort_by, sort_direction, data_source, property_type):
    match data_source:
        case "otodom":
            match property_type:
                case "apartments":
                    table_model = OtodomApartments
                case "houses":
                    table_model = OtodomHouses
                case "lands":
                    table_model = OtodomLands
                case _:
                    raise Exception(f"Invalid property type: {property_type}")
        case "domiporta":
            match property_type:
                case "apartments":
                    table_model = DomiportaApartments
                case "houses":
                    table_model = DomiportaHouses
                case "lands":
                    table_model = DomiportaLands
                case _:
                    raise Exception(f"Invalid property type: {property_type}")
        case _:
            raise Exception(f"Invalid data source: {data_source}")

    sort_column = table_model.number_id
    if sort_by:
        sort_column = dict(table_model.__table__.columns)[sort_by]

    if sort_direction in ["asc", "ASC", "ascending", "ASCENDING"]:
        query = query.order_by(sort_column.asc())
    elif sort_direction in ["desc", "DESC", "descending", "DESCENDING"]:
        query = query.order_by(sort_column.desc())

    return query
