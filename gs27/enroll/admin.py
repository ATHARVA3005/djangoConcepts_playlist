from django.contrib import admin
from .models import Student

# Register your models here.
#used decorator below
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuid', 'stuname', 'stuemail', 'stupass')
#above is the best practice for registering model class



#admin.site.register(Student, StudentAdmin)
