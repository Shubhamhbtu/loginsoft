from django.db import models
from django.utils.translation import gettext_lazy as _


class Employee(models.Model):
    name = models.CharField(_('FullName'), max_length=50)
    manager = models.ForeignKey('self', null=True,
                                blank=True,
                                related_name='employee',
                                on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name,)
