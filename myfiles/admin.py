from django.contrib import admin
from myfiles.models import *


# Register your models here.


class AdminRegistration(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'phone_number', 'region', 'school', 'test', 'date']


admin.site.register(Registration, AdminRegistration)

class AdminResult(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'tg_id', 'quiz', 'answer', 'result', 'time']


admin.site.register(Result, AdminResult)

class AdminQuestion(admin.ModelAdmin):
    list_display = ['id', 'Q', 'V1', 'V2', 'V3', 'V4', 'Answer']


admin.site.register(Question, AdminQuestion)


class AdminQuestion_ru(admin.ModelAdmin):
    list_display = ['id', 'Q', 'V1', 'V2', 'V3', 'V4', 'Answer']


admin.site.register(Question_ru, AdminQuestion_ru)



class AdminResult_ru(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'tg_id', 'quiz', 'answer', 'result', 'time']


admin.site.register(Result_ru, AdminResult_ru)


class Adminworker(admin.ModelAdmin):
    list_display = ['id', 'tg_id', 'name', 'surname', 'phone_number', 'region', 'time']


admin.site.register(Worker, Adminworker)


class AdminRegion(admin.ModelAdmin):
    list_display = ['id', 'name', ]


admin.site.register(Region, AdminRegion)


class AdminRegion_ru(admin.ModelAdmin):
    list_display = ['id', 'name', ]


admin.site.register(Region_ru, AdminRegion_ru)
