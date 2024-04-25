from typing import Any, Dict, List

from hr_etl.data_models.base import SharedBaseModel


class Employee(SharedBaseModel):
    employee_id: str
    first_name: str
    last_name: str
    department: str
    position: str
    salary: str
    date_of_birth: str


class TransformedEmployee(SharedBaseModel):
    employee_id: str
    first_name: str
    last_name: str
    full_name: str
    department: str
    position: str
    salary: int
    date_of_birth: str
    age: int


class EmployeesStructure(SharedBaseModel):
    employees_tranformed_data: List[Dict[str, Any]]
