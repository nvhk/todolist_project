from django.contrib import admin
from .models import ToDosy

# Register your models here.

class ToDosyAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)

admin.site.register(ToDosy, ToDosyAdmin)