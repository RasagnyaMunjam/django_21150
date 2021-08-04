from django.contrib import admin from .models import student,Teacher,Contract #
# Register your models here. @admin.register(student) class studentadmin(admin.ModelAdmin): list_display = ['id','name','age','fees'] @admin.register(Teacher) class Teacheradmin(admin.ModelAdmin): list_display = ['id','name','age','date','Salary']
# @admin.register(Contract) class Contractadmin(admin.ModelAdmin):
# list_display = ['id','name','age','date','payment
