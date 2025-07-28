from rest_framework.throttling import UserRateThrottle

class UserRequestPerMinutes(UserRateThrottle):
    scope="minute"

class UserRequestPerDay(UserRateThrottle):
    scope="day"
