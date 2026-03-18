from app.core.constants import (
    ERR_EMPLOYEE_EMAIL_EXISTS,
    ERR_EMPLOYEE_ID_EXISTS,
    ERR_EMPLOYEE_NOT_FOUND,
)
from app.core.exceptions import (
    EmployeeAlreadyExistsException,
    EmployeeEmailAlreadyExistsException,
    EmployeeNotFoundException,
)
from app.core.logger import get_logger
from app.repositories.employee_repository import EmployeeRepository

logger = get_logger(__name__)


class EmployeeService:
    def __init__(self) -> None:
        self.employee_repository = EmployeeRepository()

    def create_employee(self, employee_id: str, full_name: str, email: str, department: str) -> dict:
        normalized_employee_id = employee_id.strip()
        normalized_full_name = full_name.strip()
        normalized_email = email.strip().lower()
        normalized_department = department.strip()

        if self.employee_repository.get_employee_by_employee_id(normalized_employee_id):
            logger.warning("Duplicate employee_id attempted: %s", normalized_employee_id)
            raise EmployeeAlreadyExistsException(ERR_EMPLOYEE_ID_EXISTS, status_code=409)

        if self.employee_repository.get_employee_by_email(normalized_email):
            logger.warning("Duplicate employee email attempted: %s", normalized_email)
            raise EmployeeEmailAlreadyExistsException(ERR_EMPLOYEE_EMAIL_EXISTS, status_code=409)

        employee_doc = self.employee_repository.build_employee_document(
            employee_id=normalized_employee_id,
            full_name=normalized_full_name,
            email=normalized_email,
            department=normalized_department,
        )
        self.employee_repository.create_employee(employee_doc)
        logger.info("Employee created successfully: %s", normalized_employee_id)
        return employee_doc

    def get_all_employees(self) -> list[dict]:
        employees = self.employee_repository.get_all_employees()
        logger.info("Fetched %s employees.", len(employees))
        return employees

    def delete_employee(self, employee_id: str) -> None:
        normalized_employee_id = employee_id.strip()
        existing = self.employee_repository.get_employee_by_employee_id(normalized_employee_id)
        if not existing:
            logger.warning("Delete attempted for missing employee: %s", normalized_employee_id)
            raise EmployeeNotFoundException(ERR_EMPLOYEE_NOT_FOUND, status_code=404)

        self.employee_repository.delete_employee_by_employee_id(normalized_employee_id)
        logger.info("Employee deleted successfully: %s", normalized_employee_id)

    def ensure_employee_exists(self, employee_id: str) -> dict:
        normalized_employee_id = employee_id.strip()
        employee = self.employee_repository.get_employee_by_employee_id(normalized_employee_id)
        if not employee:
            logger.warning("Employee not found: %s", normalized_employee_id)
            raise EmployeeNotFoundException(ERR_EMPLOYEE_NOT_FOUND, status_code=404)
        return employee

    def count_employees(self) -> int:
        return self.employee_repository.count_employees()