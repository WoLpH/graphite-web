import models
from django.contrib import admin



class MyGraphAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'name', 'url')
    list_filter = ('profile',)
    search_fields = ('name',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'history', 'advancedUI')
    list_filter = ('user', 'advancedUI')


class VariableAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'name', 'value')
    list_filter = ('profile',)
    search_fields = ('name',)


class ViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'name')
    list_filter = ('profile',)
    search_fields = ('name',)


class WindowAdmin(admin.ModelAdmin):
    list_display = ('id', 'view', 'name', 'top', 'left', 'width', 'height',
         'url', 'interval')
    list_filter = ('view',)
    search_fields = ('name',)



admin.site.register(models.MyGraph, MyGraphAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Variable, VariableAdmin)
admin.site.register(models.View, ViewAdmin)
admin.site.register(models.Window, WindowAdmin)

