from django.contrib import admin
from .models import Pictures, Dog_pics, Tech_pics
from django.contrib.auth.models import Group


# Register your models here.

class PicsAdmin(admin.ModelAdmin):
    list_display = ['name', 'added_on']
    list_per_page = 10


class Dog_picsAdmin(admin.ModelAdmin):
    list_display = ['name', 'added_on']
    list_per_page = 10


class Tech_picsAdmin(admin.ModelAdmin):
    list_display = ['name', 'added_on']
    list_per_page = 10


admin.site.register(Pictures, PicsAdmin)
admin.site.register(Dog_pics, Dog_picsAdmin)
admin.site.register(Tech_pics, Tech_picsAdmin)
admin.site.unregister(Group)
