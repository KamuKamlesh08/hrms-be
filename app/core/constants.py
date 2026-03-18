API_HEALTH_TAG = "Health"
EMPLOYEE_TAG = "Employees"
ATTENDANCE_TAG = "Attendance"
DASHBOARD_TAG = "Dashboard"

COLLECTION_EMPLOYEES = "employees"
COLLECTION_ATTENDANCE = "attendance"

STATUS_PRESENT = "PRESENT"
STATUS_ABSENT = "ABSENT"
ALLOWED_ATTENDANCE_STATUSES = {STATUS_PRESENT, STATUS_ABSENT}

DATE_FORMAT = "%Y-%m-%d"

MSG_EMPLOYEE_CREATED = "Employee created successfully."
MSG_EMPLOYEES_FETCHED = "Employees fetched successfully."
MSG_EMPLOYEE_DELETED = "Employee deleted successfully."

MSG_ATTENDANCE_MARKED = "Attendance marked successfully."
MSG_ATTENDANCE_FETCHED = "Attendance fetched successfully."

MSG_DASHBOARD_FETCHED = "Dashboard summary fetched successfully."
MSG_HEALTH_OK = "API is healthy."

ERR_EMPLOYEE_ID_EXISTS = "Employee ID already exists."
ERR_EMPLOYEE_EMAIL_EXISTS = "Employee email already exists."
ERR_EMPLOYEE_NOT_FOUND = "Employee not found."
ERR_ATTENDANCE_ALREADY_MARKED = "Attendance already marked for this employee on this date."
ERR_INVALID_ATTENDANCE_STATUS = "Invalid attendance status. Allowed values are Present or Absent."