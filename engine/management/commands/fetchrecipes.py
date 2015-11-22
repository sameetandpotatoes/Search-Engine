from django.core.management.base import BaseCommand, CommandError
from engine import utils

class Command(BaseCommand):
    help = 'Fetches all recipes'

    def add_arguments(self, parser):
        print "Beginning script"

    def handle(self, *args, **options):
        utils.get_html("http://allrecipes.com", 4)
        self.stdout.write(self.style.SUCCESS('Successfully fetched all recipes'))
        self.stdout.write(self.style.SUCCESS('Run python manage.py update_index to update elasticsearch'))
