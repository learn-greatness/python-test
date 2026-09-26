def validate_user(user):
    """
    Validate a user dictionary.

    A valid user has:
    - non-empty string name
    - email with exactly one @
    - age between 13 and 120 inclusive
    """
    name = user["name"]
    email = user["email"]
    age = user["age"]

    if not name:
        return False

    if "@" not in email:
        return False

    if age < 13 or age > 120:
        return False

    return True
