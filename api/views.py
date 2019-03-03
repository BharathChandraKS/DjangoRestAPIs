import json
from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q
from django.http import JsonResponse
from .models import Company, People
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views
from django.core import serializers
from rest_framework.response import Response
from api.serializers import UserSerializer, GroupSerializer, CompanySerializer, PeopleSerializer,  CommonFriendSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class CommonFriends(object):
    def __init__(self, friend1, friend2, common_friends):
        self.friend1 = {"name": friend1.name,  "address": friend1.address,
                        "age": friend1.age, "phone": friend1.phone}
        self.friend2 = {"name": friend2.name, "address": friend2.address,
                        "age": friend2.age, "phone": friend2.phone}
        self.common_friends = self.brown_eyes_and_alive(
            common_friends)

    def brown_eyes_and_alive(self, friends):
        friends_lst = []
        for friend in friends:
            if friend.eyeColor == 'brown' and friend.has_died != False:
                friends_lst.append(friend.name)
        return friends_lst


class CommonFriendsView(views.APIView):
    def common_elements(self, list1, list2):
        result = []
        for element in list1:
            if element in list2:
                result.append(element)
        return result

    def get(self, request, id1, id2):
        people = People.objects.filter(index__in=(id1, id2))
        common_friends = self.common_elements(
            people[0].friends.all(), people[1].friends.all())

        result = CommonFriends(people[0], people[1], common_friends)
        serializer = CommonFriendSerializer(result)
        return Response(serializer.data)
