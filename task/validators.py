from django.core.exceptions import ValidationError


def descriptionValidator(value):
    if "bad" in value:
        raise ValidationError("Description should not contain the word 'bad'!")
    return value


def dateValidator(value):
    if "4" in str(value):
        raise ValidationError("I dislike the 4-th day of any month!")
    return value
