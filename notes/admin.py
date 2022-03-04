from django.contrib import admin

# Register your models here.
from .models import Notes,Signup

admin.site.register(Notes)
admin.site.register(Signup)
