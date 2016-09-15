from rest_framework import serializers

from cogs.models import User, Cog, Note


class CogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Cog
        fields = ('url', 'pk', 'name', 'tooth_count', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    cogs = serializers.HyperlinkedRelatedField(many=True, view_name='cog-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'user_type', 'cogs')


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ('url', 'pk', 'title', 'text', 'owner')
