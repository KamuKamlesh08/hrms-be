from typing import Any

from pydantic import BaseModel


class SuccessResponse(BaseModel):
    success: bool = True
    message: str
    data: Any | None = None


class MessageResponse(BaseModel):
    success: bool = True
    message: str