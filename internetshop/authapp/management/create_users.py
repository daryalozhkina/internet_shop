from django.core.management.base import BaseCommand

from authapp.models import KpkUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        i = 0
        while i <= 9:
            KpkUser.objects.create_user(f'user{i + 1}', f'user{i + 1}@mail.ru', password='password')
            i += 1
        KpkUser.objects.create_superuser('admin', 'admin@mail.ru', password='admin1')
        print('Пользователь создан')
