from rest_framework import serializers
from qsort.models import Program, Package, Votes
from django.contrib.auth.models import User

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = (
            "id",
            "title",
        )

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = (
            "id",
            "title",
            "program",
            "budget_level",
        )

class PackageVotesSerializer(serializers.ModelSerializer):
    total_votes = serializers.IntegerField()

    class Meta:
        model = Package
        fields = (
            "id",
            "title",
            "program",
            "budget_level",
            "cost",
            "total_votes",
        )

class VotesSerializer(serializers.ModelSerializer):

    program = serializers.SerializerMethodField()
    budget_level = serializers.SerializerMethodField()

    class Meta:
        model = Votes
        fields = (
            "id",
            "user",
            "program",
            "package",
            "budget_level",
            "votes",
        )

    def get_program(self, obj):
        program = Program.objects.get(id=obj.package.program.id)
        return program.id

    def get_budget_level(self, obj):
        return obj.package.budget_level

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )
