from rest_framework import generics
from .serializers import* 

class sendInvitation(generics.CreateAPIView):
    serializer_class = sendInvitationSerializer
