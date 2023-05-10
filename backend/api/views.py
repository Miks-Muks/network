from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404

from network.models import TopicKaif

from .serializers import TopicKaifSerializer


# Create your views here.


class TopicKaifViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        # serializer_class = TopicKaifSerializer
        queryset = get_list_or_404(TopicKaif)
        serializer_class = TopicKaifSerializer(queryset, many=True)
        return Response(serializer_class.data)
