from django.shortcuts import render
from django.http import HttpResponse
from qsort.models import Program, Package, Votes
from django.db.models import Sum

from rest_framework import viewsets
from qsort.serializers import (ProgramSerializer,
                               PackageSerializer,
                               PackageVotesSerializer,
                               VotesSerializer,
                               UserSerializer
                              )
from django.contrib.auth.models import User

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    first_program = Program.objects.get(pk=1)
    programs = Program.objects.all().prefetch_related('packages')
    
    context = {
        'first_program': first_program,
        'programs': programs
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class ProgramViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

class PackageViewSet(viewsets.ModelViewSet):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()

class PackageVotesViewSet(viewsets.ModelViewSet):
    serializer_class = PackageVotesSerializer
    queryset = Package.objects.annotate(total_votes=Sum('votes__votes')).order_by('-total_votes')

class VotesViewSet(viewsets.ModelViewSet):
    serializer_class = VotesSerializer
    queryset = Votes.objects.all()

class VotesByUser(viewsets.ModelViewSet):
    serializer_class = VotesSerializer

    def get_queryset(self):
        user_id = self.request.parser_context['kwargs']['user_id']
        return Votes.objects.filter(user__pk=user_id)

class PackagesByProgram(viewsets.ModelViewSet):
    serializer_class = PackageSerializer

    def get_queryset(self):
        user_id = self.request.parser_context['kwargs']['program_id']
        return Package.objects.filter(program__pk=user_id)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserByUsername(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
       username = self.request.parser_context['kwargs']['username']
       return User.objects.filter(username=username)