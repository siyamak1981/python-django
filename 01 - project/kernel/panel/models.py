from django.db import models
from painless.models.choices import PostStatus
# Create your models here.

status = PostStatus(is_charfield = False)
# Level (basic, normal, pro, advance, master)
class PricingTabelLevel(models.Model):
    title = models.CharField(max_length = 128)
    slug = models.CharField(max_length = 128)
    description = models.TextField( blank = True, null = True )
    severity = models.PositiveIntegerField(unique = True)


class PrcingTabel(models.Model):
    level = models.ForeignKey('PricingTabelLevel', on_delete = models.CASCADE, related_name='tabel')
    ammount = models.PositiveIntegerField()
    
    start_date = models.DateField()
    expire_date = models.DateField()
    status = models.PositiveSmallIntegerField(choices = status.get_status(), default = status.DRAFT)
    attrs = models.ManyToManyField('PricingTabelAttrs')


class PricingTabelAttrs(models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField( blank = True, null = True)
    