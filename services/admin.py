from django.contrib import admin
from django.contrib.admin.sites import site
from services.models import services
# Register your models here.
class service_admin(admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_dis')

admin.site.register(services,service_admin)