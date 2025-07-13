from django.contrib import admin
from django.utils.html import format_html

from .models import User, Unit, WorkOrder,RecertificationDocument

# Inline for WorkOrders in User + Unit
class WorkOrderInline(admin.TabularInline):
    model = WorkOrder
    extra = 0
    fields = ('job_type', 'status', 'unit', 'created_at')
    readonly_fields = ('created_at',)
    show_change_link = True

# USER ADMIN
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'full_name', 'email', 'phone_number', 'role', 'is_staff'
    )
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = (
        'username', 'email', 'first_name', 'last_name', 'middle_name', 'phone_number'
    )
    inlines = [WorkOrderInline]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.middle_name} {obj.last_name}".strip()
    full_name.short_description = 'Full Name'

#  UNIT ADMIN
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_label', 'resident', 'is_occupied')
    search_fields = ('building_name', 'unit_number', 'address')
    autocomplete_fields = ('resident',)
    inlines = [WorkOrderInline]

    def full_label(self, obj):
        return f"{obj.building_name} - {obj.unit_number}, Floor {obj.floor}"
    full_label.short_description = 'Unit'

#  WORK ORDER ADMIN
@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'job_type', 'area_type', 'area_name', 'unit', 'user',
        'status', 'created_at', 'image_preview'
    )
    list_filter = ('status', 'area_type', 'job_type')
    search_fields = ('job_type', 'description', 'area_name')
    autocomplete_fields = ('unit', 'user')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:4px" />', obj.image.url)
        return "No image"
    image_preview.short_description = 'Image'

# RECERTIFICATION ADMIN
@admin.register(RecertificationDocument)
class RecertificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'submitted_by', 'status', 'uploaded_at')
    list_filter = ('status', 'uploaded_at')
    search_fields = ('submitted_by__username', 'notes')
    autocomplete_fields = ('submitted_by',)


