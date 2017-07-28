from django.core.management.base import BaseCommand, CommandError
from addressesapp.models import Person
import csv

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
    
    def add_arguments(self, parser):
        parser.add_arguments('--output', 'store',  None, None, None, 'string', None, None, 'output file', None)

    def person_data(self, person):
        return [person.name, person.mail]
    
    def handle(self, *args, **options):
        outputfile = options['output']
        contacts = Person.objects.all()

        header = ['Name', 'email']
        f = open(outputfile, 'wb')
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(header)
        for person in contacts:
            writer.writerow(self.person_data(person))