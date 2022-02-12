import re
from django.core.exceptions import ValidationError


def phone_validator(phone):
    pattern = r'(9|(09))(((1)|(3))([0-9])|(20)|(21))(\d{7})'
    if not re.match(pattern, phone):
        raise ValidationError(f'{phone} is not a valid phone')