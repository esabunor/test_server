from rest_framework import viewsets, generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from addressesapp.serializers import AddressesSerializer
from addressesapp.models import Person

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class AddressesList(generics.ListAPIView):
    serializer_class = AddressesSerializer
    permission_classes = (AllowAny, )
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        query = self.request.query_params
        if 'name' in query:
            return Person.objects.filter(name=query['name'])
        else:
            return Person.objects.all()