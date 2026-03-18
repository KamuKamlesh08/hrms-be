from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, field_validator


class CreateEmployeeRequest(BaseModel):
    employee_id: str = Field(..., min_length=1, max_length=50)
    full_name: str = Field(..., min_length=1, max_length=120)
    email: EmailStr
    department: str = Field(..., min_length=1, max_length=100)

    @field_validator("employee_id", "full_name", "department", mode="before")
    @classmethod
    def strip_text_fields(cls, value: str) -> str:
        if isinstance(value, str):
            return value.strip()
        return value


class EmployeeResponse(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str
    created_at: datetime
    updated_at: datetime