from django.db import models


class ListField(models.TextField):
    """
    List Field represent the list of values.
    """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def to_python(self, value):
        class SubList(list):
            def __init__(self, token, *args):
                self.token = token
                super().__init__(*args)

            def __str__(self):
                return self.token.join(self)

        if isinstance(value, list):
            return value
        if value is None:
            return SubList(self.token)
        return SubList(self.token, value.split(self.token))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, (list, tuple, ListField)))
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class Company(models.Model):
    '''
    Company Model stores company details.
    '''
    index = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.company


class People(models.Model):
    """
    People Model
    """
    index = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    _id = models.CharField(max_length=64, blank=True, null=True)
    guid = models.CharField(max_length=64, blank=True, null=True)
    has_died = models.BooleanField(default=False, blank=True, null=True)
    balance = models.CharField(max_length=64, blank=True, null=True)
    picture = models.CharField(max_length=256, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    eyeColor = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    registered = models.DateTimeField(blank=True, null=True)
    greeting = models.TextField(blank=True, null=True)
    friends = models.ManyToManyField('self', blank=True, null=True)
    company = models.ForeignKey(
        Company, related_name="employees", blank=True, null=True, on_delete=models.CASCADE)
    favourite_fruits = ListField(blank=True, null=True)
    favourite_vegetables = ListField(blank=True, null=True)
    tags = ListField(blank=True, null=True)

    class Meta:
        db_table = 'people'

    def __str__(self):
        return self.name
