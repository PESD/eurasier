from django.contrib.auth.models import User
from qsort.models import Program, Package, Votes

def run():
    users = User.objects.exclude(username="admin")
    packages = Package.objects.all()
    for user in users:
        for package in packages:
            Votes.objects.get_or_create(user=user, package=package, defaults={'votes': 0})