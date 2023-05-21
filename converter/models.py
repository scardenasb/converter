from django.db import models
from django.utils.translation import gettext as _


class Type(models.Model):
    """
    Model that store unit types.
    """

    description = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("Description")
    )
    code = models.IntegerField(
        verbose_name=_("Code"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    def __str__(self):
        name = '{code} - {description}'.format(code=self.code, description=self.description)
        return name


class Unit(models.Model):
    """
    Model to create new unit, associated with type, requires exponent.
    """

    abbreviation = models.CharField(verbose_name=_("Abbreviation"),null=True, blank=True, max_length=15)
    unit_type = models.ForeignKey(
        'Type',
        verbose_name=_("Unit Type"),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    unit_exponent = models.FloatField(
        verbose_name=_("Exponent unit"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")

    def __str__(self):
        return self.abbreviation
