from django.contrib import admin
from .models import KnowledgeBaseItem, Conversation, Message, Lead


admin.site.register(KnowledgeBaseItem)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Lead)
