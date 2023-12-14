class InvalidEmailFormatError(Exception):
    pass

def validate_email(email):
    if "@" not in email or "." not in email:
        raise InvalidEmailFormatError("Invalid email format.")