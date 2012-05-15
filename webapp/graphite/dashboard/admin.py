import models
from django.contrib import admin



class DashboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    raw_id_fields = ('owners',)
    search_fields = ('name',)



admin.site.register(models.Dashboard, DashboardAdmin)

