from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@exemplo.com', 'Ibmec2026admin')
            self.stdout.write('Superuser criado')
        else:
            self.stdout.write('Superuser ja existe')