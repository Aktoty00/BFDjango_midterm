from rest_framework import serializers

from core.models import Book, Journal


class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Book
        fields = '__all__'

    def validate_num_pages(self, value):
        if value < 0:
            raise serializers.ValidationError('invalid num_pages, it must be positive')
        return value


class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = '__all__'

    def validate_type(self, value):
        if value not in ['Bullet', 'Travel', 'Food', 'Sport']:
            raise serializers.ValidationError(value + ' is not a valid choice')
        return value
