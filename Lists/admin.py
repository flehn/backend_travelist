from django.contrib import admin
from .models import TList,Element  # Import models

#Create custom admin to display ID as well in the admin panel
class TListAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'author', 'is_public', 'display_likes', 'created_at')
    list_filter = ('is_public', 'created_at', 'location')
    search_fields = ('name', 'author__username', 'location')

    def display_likes(self, obj):
        return obj.likes.count()  # Display the count of likes
    display_likes.short_description = 'Likes Count'  # Sets a more readable header for the column



# Register your model and the custom admin
admin.site.register(TList, TListAdmin)

# Register non-custom models
admin.site.register(Element)  