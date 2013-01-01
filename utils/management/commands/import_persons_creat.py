from django.core.management.base import BaseCommand, CommandError
from items.models import *
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        path = os.path.join('/Users/goldszmidt/sam/perso/dev/indexx/initialdata', 'pages_crea')
        print os.listdir(path)
        for elt in os.listdir(path):
            elt = elt.split('_')
            print elt
            first_name, last_name = elt[0], elt[1]
            Person.objects.create(first_name=first_name, last_name=last_name)
