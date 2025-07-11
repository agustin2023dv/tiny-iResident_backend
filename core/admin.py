from django.contrib import admin
from .models import User, Unit, WorkOrder

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'resident')
    search_fields = ('address',)
    autocomplete_fields = ('resident',)

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'unit', 'user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    autocomplete_fields = ('unit', 'user')
