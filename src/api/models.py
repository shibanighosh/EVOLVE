""" Module handling database connection. 

Plan is to use Tortoise ORM for handling data 
connection.
"""

# standard imports

# third-party imports
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from passlib.hash import bcrypt

# internal imports

class Users(models.Model):
    """ User model. """

    id = fields.IntField(pk=True)
    username= fields.CharField(max_length=100, unique=True)
    hashed_password = fields.CharField(max_length=255)
    email = fields.CharField(max_length=100, unique=True)
    is_logged_in = fields.BooleanField(default=False)
    last_logged_date = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    def verify_password(self, password: str):
        return bcrypt.verify(password, self.hashed_password)

user_pydantic = pydantic_model_creator(Users, name="user")
userin_pydantic = pydantic_model_creator(Users, name="userin", 
    include=('username', 'hashed_password', 'email'))
user_token_pydantic = pydantic_model_creator(Users, name="user_token",
    include=('username', 'id', 'email'))

class TimeseriesData(models.Model):
    """ Time series data model. """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    start_date = fields.DatetimeField()
    end_date = fields.DatetimeField()
    resolution_min = fields.DecimalField(max_digits=7, decimal_places=3)
    created_at = fields.DatetimeField(auto_now_add=True)
    name = fields.CharField(max_length=100)
    description = fields.CharField(max_length=255)
    image = fields.CharField(max_length=100)
    filename = fields.CharField(max_length=100)
    category = fields.CharField(max_length=100)

class ScenarioMetadata(models.Model):
    """ Scenario metadata model. """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    name = fields.CharField(max_length=100)
    description = fields.CharField(max_length=255)
    solar = fields.BooleanField()
    ev = fields.BooleanField()
    storage = fields.BooleanField()
    filename = fields.CharField(max_length=100)


class ReportMetadata(models.Model):
    """ Report metadata model. """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    name = fields.CharField(max_length=100)
    description = fields.CharField(max_length=255)
    status = fields.CharField(max_length=100)
    scenario_name = fields.CharField(max_length=100)
    report_file = fields.CharField(max_length=100)
    report_data_file = fields.CharField(max_length=100)


class Labels(models.Model):
    """ Labels model. """

    id = fields.IntField(pk=True)
    labelname = fields.CharField(max_length=100)
    username = fields.CharField(max_length=100, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

class ScenarioLabels(models.Model):
    """ Scenario label model. """
    
    id = fields.IntField(pk=True)
    scenario_id = fields.IntField()
    username = fields.CharField(max_length=100, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    labelname = fields.CharField(max_length=100)

class ReportLabels(models.Model):
    """ Report labels model ."""

    id = fields.IntField(pk=True)
    report_id = fields.IntField()
    username = fields.CharField(max_length=100, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    labelname = fields.CharField(max_length=100)

