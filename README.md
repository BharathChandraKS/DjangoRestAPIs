# Django Rest Frame Work APIs

The project has been developed using Docker Containers and Docker compose where Django and Postgres DB are run as micro services.

### Requirements

Install Docker and Docker-compose on any supported linux machine.

### Installation

```
docker-compose build
sudo docker-compose build
sudo docker-compose up -d
```

Below command creates all the fixtures to load into Postgres Database.

```
python setup/createFixtures.py
```

Migrate the Schema and Load the fixtures into the database.

```
sudo docker-compose run web python manage.py migrate
sudo docker-compose run web python manage.py loaddata api/fixtures/people.json
sudo docker-compose run web python manage.py loaddata api/fixtures/companies.json
```

If any error ensure to check that there same ports are used by two services

### APIs

Below are the APIs that can be accessed:
APIs can be accessed on "http://127.0.0.1:8000" or depending on where the service is running with the below extentions.

1. Company Details
   /company/
   /company/1/

2. People Details
   /people/
   /people/1/

3. Given 2 people display details of the 2 people and common friends who are alive and have brown eyes.
   /commonfriends/21/43/

### Test

To run Tests run the below command

sudo docker-compose run web python manage.py test
