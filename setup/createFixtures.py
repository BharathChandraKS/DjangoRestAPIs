import datetime
import json


class Person(object):

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self._id = kwargs['_id']
        self.guid = kwargs['guid']
        self.has_died = kwargs['has_died']
        self.balance = kwargs['balance']
        self.picture = kwargs['picture']
        self.age = kwargs['age']
        self.eyeColor = kwargs['eyeColor']
        self.gender = kwargs['gender']
        self.email = kwargs['email']
        self.phone = kwargs['phone']
        self.address = kwargs['address']
        self.about = kwargs['about']
        self.registered = datetime.datetime.strptime(kwargs['registered'].split(
            " -")[0], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S')
        self.greeting = kwargs['greeting']
        self.company = kwargs['company_id']
        self.favourite_fruits = self.fav_fruits(kwargs['favouriteFood'])
        self.favourite_vegetables = self.fav_vegetables(
            kwargs['favouriteFood'])
        self.tags = kwargs['tags']
        self.friends = self.friend_ids(kwargs['friends'])

    def fav_fruits(self, food_items):
        fruits_list = ["apple", "strawberry", "orange", "banana"]
        fruits = []
        for food in food_items:
            if food in fruits_list:
                fruits.append(food)
        return fruits

    def fav_vegetables(self, food_items):
        vegetables_list = ["beetroot", "celery", "carrot", "cucumber"]
        vegetables = []
        for food in food_items:
            if food in vegetables_list:
                vegetables.append(food)
        return vegetables

    def friend_ids(self, friends_lst):
        friends = []
        for friend in friends_lst:
            friends.append(friend["index"])
        return friends


def create_company_fixtures(resource, model, fixture):
    with open(resource) as f:
        data = json.load(f)
        lst = []
        for row in data:
            row_dict = {}
            row_dict["pk"] = int(row["index"])
            row_dict["model"] = model
            row_dict["fields"] = row
            lst.append(row_dict)

    with open(fixture, 'w') as outfile:
        json.dump(lst, outfile)


def create_people_fixtures(resource, model, fixture):
    with open(resource) as f:
        data = json.load(f)
        lst = []
        for row in data:
            fields = row
            row_dict = {}
            row_dict["pk"] = int(row["index"])
            row_dict["model"] = model
            person = Person(**fields)
            row_dict["fields"] = person.__dict__

            lst.append(row_dict)

    with open(fixture, 'w') as outfile:
        json.dump(lst, outfile)


# create_company_fixtures("setup/resources/companies.json", "api.company",
#                         "api/fixtures/companies.json")
create_people_fixtures("setup/resources/people.json", "api.people",
                       "api/fixtures/people.json")
