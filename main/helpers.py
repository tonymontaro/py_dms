import math


def paginate(count, limit, offset):
    """Returns pagination meta data"""
    page = math.floor(offset / limit) + 1
    page_count = math.ceil(count / limit)
    page_size = limit if (count - offset) > limit else (count - offset)

    return {'page': page,
            'page_count': page_count,
            'page_size': page_size,
            'total_count': count}


def get_query_vars(params):
    """Gets database query variables"""
    limit = int(params.get('limit', 20))
    offset = int(params.get('offset', 0))
    search = params.get('q', '')

    return limit, offset, search
