from django.contrib import admin
from .models import Profile,Category,Location,Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)