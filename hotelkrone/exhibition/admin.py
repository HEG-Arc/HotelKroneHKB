from django.contrib import admin

from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ["first_name", "last_name", "instagram_handle",]
    search_fields = ["last_name"]


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ["name", "student"]
    search_fields = ["name"]
    list_filter = ["student"]


@admin.register(models.Orte)
class OrteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name", "previous", "next", "entrance"]


@admin.register(models.POI)
class POIAdmin(admin.ModelAdmin):
    list_display = ["name", "orte", "media"]
    search_fields = ["name"]
    list_filter = ["orte"]
