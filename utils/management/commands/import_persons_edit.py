from django.core.management.base import BaseCommand, CommandError
from items.models import *
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        path = os.path.join('/Users/goldszmidt/sam/perso/dev/indexx/initialdata', 'pages_edit')
        print os.listdir(path)
        for elt in os.listdir(path):
            Person.objects.create(name=elt)
