
from mongoengine import Document
from mongoengine.fields import IntField, StringField

from hr_etl.data_models.base import SharedBaseModel


class Employee(SharedBaseModel):
    employee_id: str
    first_name: str
    last_name: str
    department: str
    position: str
    salary: str
    date_of_birth: str


class TransformedEmployee(Document):
    meta = {
        "collection": "employees",
    }
    employee_id = StringField(required=True, unique=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    full_name = StringField(required=True)
    department = StringField(required=True)
    position = StringField(required=True)
    salary = IntField(required=True)
    date_of_birth = StringField(required=True)
    age = IntField(required=True)
