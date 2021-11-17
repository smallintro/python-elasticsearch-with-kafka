from pydantic import BaseModel


class ArticleInfo(BaseModel):
    author: str = None
    title: str = None
    website: str = None
    publish_date: str = None
    has_video: bool = False


class AppResponse(BaseModel):
    status: str
    data: dict
