from fastapi import FastAPI
from starlette import status
import service.app_service as app_service
from model.data_model import ArticleInfo, AppResponse
from config.es_config import es_obj

app_v1 = FastAPI()


@app_v1.post("/v1/article/save", status_code=status.HTTP_201_CREATED, response_model=AppResponse)
def save_article_info(article: ArticleInfo):
    print(f"save_article_info: {article}")
    msg, data = app_service.save_article_info(article)
    return AppResponse(status=msg, data=data)


@app_v1.get("/v1/article/{article_id}", status_code=status.HTTP_200_OK, response_model=AppResponse)
def get_article_by_id(article_id: str):
    print(f"get_article_by_id: {article_id}")
    msg, data = app_service.get_article_by_id(article_id)
    return AppResponse(status=msg, data=data)


@app_v1.post("/v1/article/find", status_code=status.HTTP_200_OK, response_model=AppResponse)
def get_article_by_condition(article: ArticleInfo):
    print(f"get_all_article_info")
    msg, data = app_service.get_article_by_condition(article)
    return AppResponse(status=msg, data={'articles': data})


@app_v1.get("/v1/article/", status_code=status.HTTP_200_OK, response_model=AppResponse)
def get_all_articles():
    print(f"get_all_articles")
    msg, data = app_service.get_all_articles()
    return AppResponse(status=msg, data={'articles': data})


@app_v1.delete("/v1/article/{article_id}", status_code=status.HTTP_200_OK, response_model=AppResponse)
def del_article_by_id(article_id: str):
    print(f"del_article_by_id: {article_id}")
    msg, data = app_service.del_article_by_id(article_id)
    return AppResponse(status=msg, data={'result': data})


# This gets called once the app is shutting down.
@app_v1.on_event("shutdown")
async def app_shutdown():
    print('closing elasticsearch connection')
    es_obj.close()
