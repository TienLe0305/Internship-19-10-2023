from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import generics, permissions
from .models import Snippet
from .serializers import SnippetSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = [TokenHasReadWriteScope]
    permission_classes = [permissions.IsAuthenticated]
    
    
class SnippetDetail(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = [TokenHasReadWriteScope]
    permission_classes = [permissions.IsAuthenticated]