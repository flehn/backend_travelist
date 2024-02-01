from django.contrib import admin
from .models import TList,Element  # Import models

#Create custom admin to display ID as well in the admin panel
class TListAdmin(admin.ModelAdmin):
    # This will display these fields in the Django admin list view
    list_display = ('id', 'name', 'city', 'author', 'created_at')

# Register your model and the custom admin
admin.site.register(TList, TListAdmin)

# Register non-custom models
admin.site.register(Element)  