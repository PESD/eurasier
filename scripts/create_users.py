from django.contrib.auth.models import User
from qsort.models import Program, Package, Votes
from random import randint


def run():
    NUM_USERS = 30

    while NUM_USERS > 0:
        username = str(randint(1000, 9999))
        user = User.objects.create_user(username, username + '@phxschools.org', 'phoenix')
        programs = Program.objects.all()
        for program in programs:
            packages = Package.objects.all()
            for package in packages:
                Votes.objects.create(user=user, package=package, votes=0)
        NUM_USERS = NUM_USERS - 1
