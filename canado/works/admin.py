from django.contrib import admin
from .models import Works

# Register your models here.

# @admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('darbas','c_remarks', 'pareigos','start_time', 'end_time', 'skaiciuoti_uzmokesti')
    list_filter = ('pareigos','c_remarks', 'start_time', 'end_time')
    search_fields = ('darbas',)
    list_per_page = 20


admin.site.register(Works, WorksAdmin)



