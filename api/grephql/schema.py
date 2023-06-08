from graphene import relay
import graphene
from graphene_django import DjangoObjectType
from table.models.test import Test

class TestsObject(DjangoObjectType):
    class Meta:
        model = Test

class Query(graphene.ObjectType):
    # _a : A 이런식으로 언더바가 대문자를 뜻함
    # ===========================
    # List : 리스트 타입 반환 , Fild : 단일 인스턴스만 반환 즉 하나만 반환
    # all = graphene.List(TestsObject)
    test = graphene.String() # 쿼리에서 사용되는 문장이다 ex) query { test { name, money }}

    def resolve_test(root, info): # 함수 이름은 resolve_쿼리에서 정의한 이름 이 나와야 한다
        # 리턴값은 다음과 같은 쿼리셋이 나와야한다 (<QuerySet [<Book: Book object (하나)>]>)
        return 'Hi?'
        # return Test.objects.all()

schema = graphene.Schema(query=Query)