from django.core.exceptions import ValidationError


def validate_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError('Please choose a PNG file.')