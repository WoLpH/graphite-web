import models
from django.contrib import admin



class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'when', 'what', 'data', 'tags')
    list_filter = ('when',)



admin.site.register(models.Event, EventAdmin)

