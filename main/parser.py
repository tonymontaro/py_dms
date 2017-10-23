from djangorestframework_camel_case.util import underscoreize
from rest_framework import parsers
from django.conf import settings
from django.http import QueryDict


class CamelCaseFormParser(parsers.FormParser):
    def parse(self, stream, media_type=None, parser_context=None):
        print('======here=======')
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        data = QueryDict(stream.read(), encoding=encoding)
        return underscoreize(data)
