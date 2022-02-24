from django.contrib import admin
from .models import Post
from .models import CustomerHBD
from .models import dummy

admin.site.register(Post)
admin.site.register(CustomerHBD)
admin.site.register(dummy)
