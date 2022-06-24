from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ValidationError
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer, CommentSerializer, VoteSerializer
from .models import Movie, Comment, Vote
from .pagination import CustomPagination
from .filters import MovieFilter
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class ListCreateCommentAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Comment.objects.filter(movie=self.kwargs['pk'])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, movie_id=self.kwargs['pk'])

class RetrieveUpdateDestroyCommentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_url_kwarg = 'comment_pk'

    def get_queryset(self):
        return Comment.objects.filter(id=self.kwargs['comment_pk']).filter(movie_id=self.kwargs['pk'])

class ListCreateVoteAPIView(ListCreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Vote.objects.filter(movie=self.kwargs['pk'])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, movie_id=self.kwargs['pk'])

class RetrieveUpdateDestroyVoteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_url_kwarg = 'vote_pk'

    def get_queryset(self):
        return Vote.objects.filter(id=self.kwargs['vote_pk']).filter(movie_id=self.kwargs['pk'])
    

