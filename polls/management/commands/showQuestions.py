from django.core.management.base import BaseCommand
from polls.models import Question as Poll

class Command(BaseCommand):
    def handle(self, *args, **options):
        results = Poll.objects.all()
        for result in results:
            print(result)