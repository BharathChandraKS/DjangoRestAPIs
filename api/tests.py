from django.test import TestCase
from rest_framework import status
from .models import People, Company
from rest_framework.test import APIClient


class ParuanaraTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person1 = {
            'name': 'Carmella Lambert',
            'index': 1,
            "_id": "595eeb9b96d80a5bc7afb106",
            "guid": "5e71dc5d-61c0-4f3b-8b92-d77310c7fa43",
            "has_died": True,
            "balance": "$2,418.59",
        }
        self.person2 = {
            'name': 'Bonnie Bass',
            'index': 2,
            "_id": "595eeb9b1e0d8942524c98ad",
            "guid": "b057bb65-e335-450e-b6d2-d4cc859ff6cc",
            "has_died": False,
            "balance": "$1,562.58",
        }
        company1 = Company(index=1, company="GAZAK")
        company2 = Company(index=2, company="QOT")
        people1 = People(company=company1, **self.person1)
        people2 = People(company=company2, **self.person2)
        company1.save()
        company2.save()
        people1.save()
        people2.save()

    def test_people_get(self):
        response = self.client.get('/people/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.person1['name'])

    def test_company_get(self):
        response = self.client.get('/company/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
