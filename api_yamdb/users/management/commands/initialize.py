import csv
import logging
import os

from django.core.management.base import BaseCommand

from users.models import User

_logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Fill data to models'

    @staticmethod
    def load_data(file_name, class_name):
        path = os.path.join(file_name)
        with open(path) as f:
            reader = csv.reader(f)
            data_dict = []
            for row in reader:
                if reader.line_num == 1:
                    keys = row
                    fields = [i.attname for i in class_name._meta.fields]
                    for fname in keys:
                        if fname not in fields:
                            print(f'========= Removing {fname}!!!')
                            keys.remove(fname)
                if reader.line_num > 1:
                    row_dict = {}
                    for i, key in enumerate(keys):
                        row_dict[key] = row[i]
                    data_dict.append(row_dict)
                    obj, is_created = (
                        class_name.objects.get_or_create(**row_dict)
                    )
                    print(obj, is_created)

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs='+', type=str)

    def handle(self, *args, **options):
        for file_name in options.get('file_name'):
            if file_name == 'users':
                self.load_data(f'./data/{file_name}.csv', User)

        self.stdout.write("Done!")
