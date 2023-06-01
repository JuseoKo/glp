from django.contrib import admin
from table.models import Book, Cash
from django import forms

class BookAdminForm(forms.ModelForm):
    # (지정값, 표시레이블)
    CHOICES = [
        ('maria', 'Maria'),
        ('sophia', 'Sophia'),
    ]
    # name필드를 드롭다운으로 표기
    name = forms.ChoiceField(choices=CHOICES)
    # 모델을 Book로 지정하고 사용할 필드 지정
    class Meta:
        model = Book
        fields = ('name', 'number')


class BookAdmin(admin.ModelAdmin):
    # from을 BookAdminForm에 있는 폼으로 사용하겠다
    form = BookAdminForm

# 모델 등록
admin.site.register(Book, BookAdmin)


