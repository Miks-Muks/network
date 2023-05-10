from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def check_mate(value):
    mate = 'блять'
    check = value.split()
    if mate in value:
        raise ValidationError(
            _("%(value)s is a mate.Wanring"),
            params={"value": value},
        )
