from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Имя режиссера не должно быть пустым.")
        return value


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all())

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Название фильма не должно быть пустым.")
        return value

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Продолжительность фильма должна быть положительным числом.")
        return value


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Review
        fields = '__all__'

    def validate_text(self, value):
        if not value:
            raise serializers.ValidationError("Текст отзыва не должен быть пустым.")
        return value

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Рейтинг отзыва должен быть от 1 до 5.")
        return value
