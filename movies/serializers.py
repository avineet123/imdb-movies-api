from .models import Movie, Genre
from rest_framework import exceptions
from rest_framework import serializers

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('name', 'imdb_score', 'popularity', 'director', 'genre')

    def to_representation(self, instance):
        ret = super(MovieSerializer, self).to_representation(instance)
        ret['99popularity'] = ret['popularity']
        del ret['popularity']
        return ret

    def to_internal_value(self, data):
        popularity = data.get('99popularity')
        # validation for popularity_99
        if not popularity:
            raise exceptions.ValidationError({
                '99popularity': 'This field is required.'
            })
        else:
            if float(popularity) > 100.0 or float(popularity) < 0:
                raise exceptions.ValidationError({
                    '99popularity':
                        'This field value should be between 0 to 100.'
                })

        director = data.get('director')
        # validation for director
        if not director:
            raise exceptions.ValidationError({
                'director': 'This field is required.'
            })

        genre = data.get('genre')

        imdb_score = data.get('imdb_score')
        # validation for imdb_score
        if not imdb_score:
            raise exceptions.ValidationError({
                'imdb_score': 'This field is required.'
            })
        else:
            if float(imdb_score) > 10.0 or float(imdb_score) < 0:
                raise exceptions.ValidationError({
                    'imdb_score':
                        'This field value should be between 0 to 10.'
                })

        name = data.get('name')
        # validation for director
        if not name:
            raise exceptions.ValidationError({
                'name': 'This field is required.'
            })

        return {
            'popularity': float(popularity),
            'director': director,
            'genre': genre,
            'imdb_score': float(imdb_score),
            'name': name
        }

    def create(self, validated_data):
        new_movie = Movie(name=validated_data['name'],
                               director=validated_data['director'],
                               popularity=validated_data['popularity'],
                               imdb_score=validated_data['imdb_score']
                               )
        new_movie.save()
        # add genre
        for genre in validated_data['genre']:
            obj, created = Genre.objects.get_or_create(name=genre)
            new_movie.genre.add(obj)
        return new_movie

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.popularity_99 = validated_data.get('popularity',
                                                    instance.popularity_99)
        instance.imdb_score = validated_data.get('imdb_score',
                                                 instance.imdb_score)
        instance.director = validated_data.get('director', instance.director)
        # update genre
        instance.genre = []
        for genre in validated_data['genre']:
            obj, created = Genre.objects.get_or_create(name=genre)
            instance.genre.add(obj)
        instance.save()
        return instance
