from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'program', views.ProgramViewSet, 'program')
router.register(r'package', views.PackageViewSet, 'package')
router.register(r'package-votes', views.PackageVotesViewSet, 'package-votes')
router.register(r'votes', views.VotesViewSet, 'votes')
router.register(r'user', views.UserViewSet, 'user')
router.register(r'user-by-username/(?P<username>[0-9]+)', views.UserByUsername, 'user-by-username')
router.register(r'votes-by-user/(?P<user_id>[0-9]+)', views.VotesByUser, 'votes-by-user')
router.register(r'packages-by-program/(?P<program_id>[0-9]+)', views.PackagesByProgram, 'packages-by-program')


urlpatterns = [
    url(r'^', include(router.urls)),
    # path('', views.index, name='index'),
]