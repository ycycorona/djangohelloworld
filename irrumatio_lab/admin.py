from django.contrib import admin

from .models import Actress, ProductionEvaluation, ProductionAddons, ReviewImg,\
    Production

admin.site.register(Actress)
admin.site.register(ProductionEvaluation)
admin.site.register(ProductionAddons)
admin.site.register(ReviewImg)
admin.site.register(Production)
# Register your models here.
