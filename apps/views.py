from rest_framework.viewsets import ModelViewSet

from apps.filters import WriterFilter, PublisherFilter, SubjectFilter
from apps.models import Book, Writer, Publisher, Subject
from apps.serializers import BookModelSerializer, WriterModelSerializer, PublisherModelSerializer, \
    SubjectModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class WriterModelViewSet(ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterModelSerializer
    filterset_class = WriterFilter


class PublisherModelViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer
    filterset_class = PublisherFilter


class SubjectModelViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectModelSerializer
    filterset_class = SubjectFilter
