from graphene import Schema
from app.graphql.mutations import Mutation
from app.graphql.queries import Query

schema = Schema(query=Query, mutation=Mutation)
