import math


def paginate(count, limit, offset):
    page = math.floor(offset / limit) + 1
    page_count = math.ceil(count / limit)
    page_size = limit if (count - offset) > limit else (count - offset)

    return {'page': page, 'page_count': page_count, 'page_size': page_size, 'total_count': count}
