from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    """
    list all snippets or create new one.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve, update, or delete a code snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
