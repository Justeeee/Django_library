from rest_framework.serializers import ModelSerializer

from apps.models import Subject, Book, Publisher, Writer


class SubjectModelSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name',)


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class PublisherModelSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'description')


class WriterModelSerializer(ModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'


