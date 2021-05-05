from django.contrib import admin
from . import models
# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    fields = ['name','slug','description']

    search_fields = ['name','slug']

    list_display = ['name','slug']

    list_editable = ['slug']

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group,GroupAdmin)
