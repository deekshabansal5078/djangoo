from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

from tutorial.quickstart.serializers import CigarSerializer
from tutorial.quickstart.models import Cigar
from rest_framework import response
from rest_framework import decorators

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
# Create your views here.


  # from rest_framework.decorators import action, link, api_view
    def action():
        return lambda func: decorators.detail_route(methods=['post'])(func)

    def link():
        return lambda func: decorators.detail_route()(func)

class CigarViewSet(viewsets.ModelViewSet):

    """ Cigar resource. """

    serializer_class = CigarSerializer
    model = Cigar
    queryset = Cigar.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Return a list of objects.

        """
        return super(CigarViewSet, self).list(request, *args, **kwargs)

    def action():
        return lambda func: decorators.detail_route(methods=['post'])(func)

    def link():
        return lambda func: decorators.detail_route()(func)



    @action()
    def set_price(self, request, pk):
        """An example action to on the ViewSet."""
        return Response('20$')

    @link()
    def get_price(self, request, pk):
        """Return the price of a cigar."""
        return Response('20$')