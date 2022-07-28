from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Class, Review, Apply

admin.site.register(User)
admin.site.register(Class)
admin.site.register(Review)
admin.site.register(Apply)