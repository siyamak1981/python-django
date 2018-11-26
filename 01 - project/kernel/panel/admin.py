from django.contrib import admin
from khayyam import JalaliDate as jd

from . import models

# Register your models here.


@admin.register(models.PrcingTabel)
class PrcingTabelAdmin(admin.ModelAdmin):
    pass

@admin.register(models.PricingTabelLevel)
class PricingTabelLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(models.PricingTabelAttrs)
class PricingTabelAttrsAdmin(admin.ModelAdmin):
    pass