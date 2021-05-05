from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    fields = ['group','message','user']

    search_fields = ['message']

    list_filter = ['group','user']

    list_display = ['group','message']


# Register your models here.
admin.site.register(models.Post,PostAdmin)
