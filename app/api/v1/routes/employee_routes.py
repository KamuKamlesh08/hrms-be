from fastapi import APIRouter, status

from app.core.constants import (
    EMPLOYEE_TAG,
    MSG_EMPLOYEE_CREATED,
    MSG_EMPLOYEE_DELETED,
    MSG_EMPLOYEES_FETCHED,
)
from app.schemas.common_schema import MessageResponse, SuccessResponse
from app.schemas.employee_schema import CreateEmployeeRequest, EmployeeResponse
from app.services.employee_service import EmployeeService

router = APIRouter(prefix="/employees", tags=[EMPLOYEE_TAG])
employee_service = EmployeeService()


@router.post("", response_model=SuccessResponse, status_code=status.HTTP_201_CREATED)
def create_employee(payload: CreateEmployeeRequest) -> SuccessResponse:
    employee = employee_service.create_employee(
        employee_id=payload.employee_id,
        full_name=payload.full_name,
        email=payload.email,
        department=payload.department,
    )
    return SuccessResponse(message=MSG_EMPLOYEE_CREATED, data=EmployeeResponse(**employee))


@router.get("", response_model=SuccessResponse, status_code=status.HTTP_200_OK)
def get_all_employees() -> SuccessResponse:
    employees = employee_service.get_all_employees()
    data = [EmployeeResponse(**employee) for employee in employees]
    return SuccessResponse(message=MSG_EMPLOYEES_FETCHED, data=data)


@router.delete("/{employee_id}", response_model=MessageResponse, status_code=status.HTTP_200_OK)
def delete_employee(employee_id: str) -> MessageResponse:
    employee_service.delete_employee(employee_id)
    return MessageResponse(message=MSG_EMPLOYEE_DELETED)