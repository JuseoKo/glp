from graphene import relay
import graphene
from graphene_django import DjangoObjectType
from table.models.book import Book


"""
query{
  allBook(number: "your_number_here") { # allBook
    Name
    number
  }
}
"""

class Books(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("Name", "number")

class Query(graphene.ObjectType):
    all_Book = graphene.List(Books)
    print(Book.objects.all())
    def resolve_all_book(root, info):
        return Book.objects.all()

schema = graphene.Schema(query=Query)