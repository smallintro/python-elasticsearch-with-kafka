from elasticservice import es_service as es
from kafkaservice import kafka_producer as kfk
from appmodel.data_model import ArticleInfo


def save_article_info(article: ArticleInfo):
    try:
        response = es.add_doc_to_index(article)
        if response.get('result') == 'created':
            return "success", {response['result']: response['_id']}
        else:
            return "failed", {response['result']: None}
    except Exception as ex:
        # send a failure message to generate alarm
        kfk.publish_message(str(ex))
        return "failed", str(ex)


def get_article_by_id(article_id):
    try:
        data = {}
        response = es.get_article_by_id(article_id)
        for hits in response['hits']['hits']:
            data[hits['_id']] = hits['_source']
        return "success", data
    except Exception as ex:
        # send a failure message to generate alarm
        kfk.publish_message(str(ex))
        return "failed", str(ex)


def get_all_articles():
    try:
        data = {}
        response = es.get_all_articles()
        for hits in response['hits']['hits']:
            data[hits['_id']] = hits['_source']
        return "success", data
    except Exception as ex:
        # send a failure message to generate alarm
        kfk.publish_message(str(ex))
        return "failed", str(ex)


def del_article_by_id(article_id):
    try:
        response = es.delete_article_by_id(article_id)
        return "success", response['result']
    except Exception as ex:
        # send a failure message to generate alarm
        kfk.publish_message(str(ex))
        return "failed", str(ex)


def get_article_by_condition(article: ArticleInfo):
    try:
        data = {}
        response = es.get_article_by_author(article.author)
        for hits in response['hits']['hits']:
            data[hits['_id']] = hits['_source']
        return "success", data
    except Exception as ex:
        # send a failure message to generate alarm
        kfk.publish_message(str(ex))
        return "failed", str(ex)
