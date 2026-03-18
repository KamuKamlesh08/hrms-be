from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from app.core.constants import DATE_FORMAT


class MarkAttendanceRequest(BaseModel):
    employee_id: str = Field(..., min_length=1, max_length=50)
    date: str = Field(..., min_length=10, max_length=10)
    status: str = Field(..., min_length=1, max_length=20)

    @field_validator("employee_id", "status", mode="before")
    @classmethod
    def strip_text_fields(cls, value: str) -> str:
        if isinstance(value, str):
            return value.strip()
        return value

    @field_validator("date")
    @classmethod
    def validate_date_format(cls, value: str) -> str:
        datetime.strptime(value, DATE_FORMAT)
        return value


class AttendanceResponse(BaseModel):
    employee_id: str
    date: str
    status: str
    created_at: datetime
    updated_at: datetime