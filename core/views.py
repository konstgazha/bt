from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from core.serializers import UserSerializer, GroupSerializer
from core.models import Organization


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OrganizationsView(View):
    def get(self, request):
        organizations = Organization.objects.all()
        return HttpResponse(organizations)