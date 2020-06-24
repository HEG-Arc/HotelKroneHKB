from django.contrib import admin

from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ["first_name", "last_name", "instagram_handle",]
    search_fields = ["last_name"]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "orten":
            kwargs["queryset"] = models.Orte.objects.filter(poi__media__student_id=request.resolver_match.kwargs['object_id']).distinct()
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ["name", "student", "order"]
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


@admin.register(models.TrackedFile)
class TrackedFileAdmin(admin.ModelAdmin):
    list_display = ["name", "student", "counter"]
    list_filter = ["student"]


@admin.register(models.ContentManagement)
class ContentManagementAdmin(admin.ModelAdmin):
    pass
