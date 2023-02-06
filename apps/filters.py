from django_filters.rest_framework import FilterSet

from apps.models import Book, Writer, Publisher, Subject


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = ['name', 'writer', 'subjects']


class WriterFilter(FilterSet):
    class Meta:
        model = Writer
        fields = ['first_name', 'last_name', ]


class PublisherFilter(FilterSet):
    class Meta:
        model = Publisher
        fields = ['name', ]


class SubjectFilter(FilterSet):
    class Meta:
        model = Subject
        fields = ['name', ]
