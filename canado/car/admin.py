from django.contrib import admin
from .models import Car, Image

# Register your models here.
admin.register(Car)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

class CarAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project_resume",
        "Gamintojas",
        "Marke",
        "Variklis",
        "Galia",
        "Spalva",
        "Metai",
        "project_start_date",
        "project_status",

    )
    list_filter = ("Gamintojas", "Marke", "Variklis", "Galia", "Spalva","Metai", "project_status")
    search_fields = ("title", "project_resume")
    list_per_page = 20
    date_hierarchy = "c_created_at"
    readonly_fields = ("c_created_at", "c_updated_at")
    fieldsets = (
        ("Basic Information", {"fields": ("title", "project_resume")}),
        ("Manufacturer and Engine", {"fields": ("Gamintojas", "Marke", "Variklis", "Galia")}),
        ("Color and Details", {"fields": ("Spalva", "Metai")}),
        ("Project Information", {"fields": ("project_start_date", "project_status")}),
        ("Additional Information", {"fields": ("c_remarks", "c_created_at", "c_updated_at")}),
    )
    inlines = [ImageInline]

admin.site.register(Car, CarAdmin)
