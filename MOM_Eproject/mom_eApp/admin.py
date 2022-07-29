from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Class, Review, Apply, Qna

admin.site.register(User)
admin.site.register(Class)
admin.site.register(Apply)
admin.site.register(Qna)
admin.site.register(Review)