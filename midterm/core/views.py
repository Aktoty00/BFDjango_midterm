from rest_framework import viewsets
from rest_framework import mixins

from core.models import Book, Journal
from core.serializer import BookSerializer, JournalSerializer


class BookListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class JournalListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
