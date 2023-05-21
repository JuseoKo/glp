from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'My custom command'

    def handle(self, *args, **options):
        # 커맨드 실행 로직 작성
        from table.models.book import Book
        Book.objects.create(Name='하나', number='주황')