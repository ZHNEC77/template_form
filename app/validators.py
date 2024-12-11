import re


def validate_date(value):
    date_pattern1 = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
    date_pattern2 = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(date_pattern1.match(value) or date_pattern2.match(value))


def validate_phone(value):
    phone_pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    return bool(phone_pattern.match(value))


def validate_email(value):
    email_pattern = re.compile(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(email_pattern.match(value))


def get_field_type(value):
    if validate_date(value):
        return 'date'
    elif validate_phone(value):
        return 'phone'
    elif validate_email(value):
        return 'email'
    else:
        return 'text'
