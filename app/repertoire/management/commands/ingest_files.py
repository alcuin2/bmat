import os
import csv
from django.core.management.base import BaseCommand

from repertoire.models import File, Work

class Command(BaseCommand):
    help = 'Ingest CSV files to DB'

    def handle(self, *args, **kwargs):
        try:
            count = File.objects.all().count()
            if count == 0:
                print("Seeding data")
                files = os.listdir('./files')
                for csv_file in files:
                    new_file = File()
                    new_file.filename = csv_file
                    with open('./files/' + csv_file, 'r') as file:
                        reader = csv.reader(file)
                        next(reader) # skip headers
                        row_count = 0
                        list_of_works = []
                        for row in reader:
                            new_work = Work()
                            new_work.file = new_file
                            new_work.title = row[0]
                            new_work.contributors = row[1].split("|")
                            new_work.iswc = row[2]
                            new_work.source = row[3]
                            new_work.proprietary_id = row[4]
                            row_count += 1
                            list_of_works.append(new_work)
                        new_file.work_count = row_count
                        new_file.save()
                        for work in list_of_works:
                            work.save()
        except:
            print("Seeding failed")
            
        

