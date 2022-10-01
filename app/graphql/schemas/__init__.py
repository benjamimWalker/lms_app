from graphene import Schema
from app.graphql.queries import Query

schema = Schema(query=Query)
