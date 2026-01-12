from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Conversation, Message


@api_view(["POST"])
def chat(request):
    text = request.data.get("message")
    conv_id = request.data.get("conversation_id")

    if not text:
        return Response({"error": "No message provided"}, status=400)

    if conv_id:
        conversation = Conversation.objects.get(id=conv_id)
    else:
        conversation = Conversation.objects.create()

    Message.objects.create(
        conversation=conversation,
        role="user",
        content=text
    )

    # Simple placeholder response
    reply = "Thanks for your message! We'll get back to you shortly."

    Message.objects.create(
        conversation-conversation,
        role="bot",
        cotent=reply
    )

    return Response({
        "reply": reply,
        "conversation_id": conversation.id
    })
