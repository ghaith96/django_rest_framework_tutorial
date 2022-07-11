from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User

from .permissions import IsOwnerOrReadOnly

from .serializers import UserSerialzer

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    """
    list all snippets or create new one.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes= [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve, update, or delete a code snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes= [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzer

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
