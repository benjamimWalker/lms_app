import uvicorn
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from app.graphql.schemas import schema

app = FastAPI()

app.mount('/g', GraphQLApp(schema=schema, on_get=make_graphiql_handler()))

if __name__ == '__main__':
    uvicorn.run(app)
