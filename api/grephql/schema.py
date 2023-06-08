from graphene import relay
import graphene
from graphene_django import DjangoObjectType
from table.models.test import Test

class Tests(DjangoObjectType):
    class Meta:
        model = Test

class Query(graphene.ObjectType):
    # _a : A 이런식으로 언더바가 대문자를 뜻함
    # all = graphene.List(Books)
    # ===========================
    # List : 리스트 타입 반환 , Fild : 단일 인스턴스만 반환 즉 하나만 반환
    all = graphene.List(Tests, args={
        "number": graphene.String(required=False),
    })

    def resolve_all(root, info, number = None):

        # 리턴값은 다음과 같은 쿼리셋이 나와야한다 (<QuerySet [<Book: Book object (하나)>]>)
        if number != None:
            return Book.objects.filter(number=number)
        else:
            return Book.objects.all()

schema = graphene.Schema(query=Query)