from .models import Company, People
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class CommonFriendSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            'person1': obj.friend1,
            'person2': obj.friend2,
            'common_friends': obj.common_friends,
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    employees = serializers.StringRelatedField(many=True)

    def validate(self, employees):
        """
        Check that the start is before the stop.
        """
        if employees.len == 0:
            return "No Employees Found"
        return employees

    class Meta:
        model = Company
        fields = ('url', 'company', 'employees')


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = ('url', 'name', 'has_died', 'balance', 'picture', 'age', 'eyeColor', 'gender', 'email', 'phone',
                  'address', 'about', 'registered', 'greeting', 'company', 'favourite_fruits', 'favourite_vegetables')
