from graphene import relay
import graphene
from graphene_django import DjangoObjectType
from table.models.news import NewsValues
from table.models.news import BaseNews

class NewsObject(DjangoObjectType):
    pass
    class Meta:
        model = NewsValues

class BaseNewsObject(DjangoObjectType):
    class Meta:
        model = BaseNews

class Query(graphene.ObjectType):
    # _a : A 이런식으로 언더바가 대문자를 뜻함
    # List : 리스트 타입 반환 , Fild : 단일 인스턴스만 반환 즉 하나만 반환
    # ===========================
    # 쿼리에서 사용되는 문장이다 ex) query { base { name, money }}, query { news { name, money }}
    base = graphene.Field(BaseNewsObject, newscode=graphene.String())
    news = graphene.Field(NewsObject, id=graphene.Int())

    def resolve_news(root, info, id=None): # 함수 이름은 resolve_쿼리에서 정의한 이름 이 나와야 한다
        """
        [쿼리]
        query{ news(id : 1)
            {
                id,
                value
            }
        }
        """
        return NewsValues.objects.filter(id=id)[0]
    def resolve_base(root, info, newscode=None):
        """
        쿼리 :
        query($newscode: String!) {
          base(newscode: $newscode) {
            newsCode
          }
        }
        [input]
        {
          "newscode": "01"
        }
        """
        return BaseNews.objects.filter(news_code=newscode)[0]

schema = graphene.Schema(query=Query)