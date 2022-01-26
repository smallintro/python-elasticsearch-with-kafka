import json
from elasticservice.es_config import es_obj, default_index


def add_doc_to_index(document_data, index_name=default_index):
    try:
        document_json_data = json.dumps(document_data.__dict__)
        response = es_obj().index(index=index_name, doc_type='_doc', body=document_json_data)
        print(response)
        return response
    except Exception as ex:
        print('Error while add_doc_to_index: %s' % str(ex))
        raise ex


def get_article_by_author(author, index_name=default_index):
    # exact match:- {'query': {'term': {'author': author}}}
    search_object = {'query': {'match': {'author': author}}}
    try:
        response = es_obj().search(index=index_name, body=json.dumps(search_object))
        print(response)
        return response
    except Exception as ex:
        print('Error while get_article_by_author: %s' % str(ex))
        raise ex


def get_article_by_id(article_id, index_name=default_index):
    search_object = {'query': {'ids': {'values': [article_id]}}}
    try:
        response = es_obj().search(index=index_name, body=json.dumps(search_object))
        print(response)
        return response
    except Exception as ex:
        print('Error while get_article_by_id: %s' % str(ex))
        raise ex


def get_all_articles(index_name=default_index):
    try:
        response = es_obj().search(index=index_name)
        print(response)
        return response
    except Exception as ex:
        print('Error while get_all_articles: %s' % str(ex))
        raise ex


def delete_article_by_id(article_id, index_name=default_index):
    try:
        # delete_by_query(index, body)
        response = es_obj().delete(index=index_name, ignore=404, id=article_id)
        print(response)
        return response
    except Exception as ex:
        print('Error while delete_article_by_id: %s' % str(ex))
        raise ex


'''if __name__ == "__main__":
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/full-text-queries.html
    article_data = {
        "author": "Sushil",
        "title": "Small intro to elasticsearch python API",
        "website": "smallintro.github.io",
        "publish_date": "2021-11-14",
        "has_video": True,
    }
    create_index(default_index)
    add_doc_to_index(article_data, default_index)
    get_doc_from_index(default_index)'''
