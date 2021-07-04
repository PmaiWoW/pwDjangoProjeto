from django.contrib import admin

from .models import Agent, Message, Quiz, Comment

# Register your models here.
admin.site.register(Agent)
admin.site.register(Message)
admin.site.register(Quiz)
admin.site.register(Comment)