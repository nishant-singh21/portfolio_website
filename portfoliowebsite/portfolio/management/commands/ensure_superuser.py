import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        'Create or update a superuser from DJANGO_SUPERUSER_USERNAME, '
        'DJANGO_SUPERUSER_EMAIL and DJANGO_SUPERUSER_PASSWORD environment '
        'variables. Safe to run on every deploy.'
    )

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not username or not password:
            self.stdout.write(
                self.style.WARNING(
                    'DJANGO_SUPERUSER_* env vars not set — skipping superuser setup.'
                )
            )
            return

        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(
            username=username,
            defaults={'email': email},
        )

        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Superuser "{username}" '
                f'{"created" if created else "updated"} from environment variables.'
            )
        )
