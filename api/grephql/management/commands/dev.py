from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'My custom command'

    def handle(self, *args, **options):
        # 커맨드 실행 로직 작성
        import bardapi
        import os
        os.environ['_BARD_API_KEY'] = 'WwhgnwX5QtrnLMhhPxuTOytu2bzZwZRyxoJsIa6uoG8kedYITApdXCNMXcPm-NfLqGTlmQ.'
        input_test = '좋은 저녁이야'
        response = bardapi.core.Bard().get_answer(input_test)
        print(response)