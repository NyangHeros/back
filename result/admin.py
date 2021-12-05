from result.models import Photos, Results
from django.contrib import admin

# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(Photos, ResultAdmin)
admin.site.register(Results, ResultAdmin)
