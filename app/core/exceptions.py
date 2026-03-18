class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400, details: dict | None = None) -> None:
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(message)


class EmployeeAlreadyExistsException(AppException):
    pass


class EmployeeEmailAlreadyExistsException(AppException):
    pass


class EmployeeNotFoundException(AppException):
    pass


class AttendanceAlreadyMarkedException(AppException):
    pass


class InvalidAttendanceStatusException(AppException):
    pass