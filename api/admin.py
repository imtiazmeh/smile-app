from django.contrib import admin
from api.v1.models import Student
# Register your models here.


@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'roll_no', 'city']
