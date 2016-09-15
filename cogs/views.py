from rest_framework import viewsets

from cogs.models import User, Cog, Note, PersonalNote
from cogs.serializers import UserSerializer, CogSerializer, NoteSerializer
from cogs.permissions import CogmakerOrReadOnly, SameTypeOnly, OwnerOnly


class CogViewSet(viewsets.ModelViewSet):
    queryset = Cog.objects.all()
    serializer_class = CogSerializer
    permissions_classes = (CogmakerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permissions_classes = (SameTypeOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PersonalNoteViewSet(viewsets.ModelViewSet):
    queryset = PersonalNote.objects.all()
    serializer_class = NoteSerializer
    permissions_classes = (OwnerOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
