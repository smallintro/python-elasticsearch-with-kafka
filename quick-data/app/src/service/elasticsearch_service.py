from elasticsearch import Elasticsearch
import json
import logging
import requests

_es_obj = None


def init_elasticsearch():
    global _es_obj
    _es_obj = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es_obj.ping():
        print('Elasticsearch Connected')
        res = requests.get('http://localhost:9200')
        print(res.content)
        return True
    else:
        print('Elasticsearch not connected')
        return False


def es_obj():
    global _es_obj
    if _es_obj is None:
        init_elasticsearch()
    return _es_obj


def create_index(index_name):
    result = False
    # index settings
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        },
        "mappings": {
            "dynamic": "strict",
            "properties": {
                "author": {"type": "text"},
                "title": {"type": "text"},
                "website": {"type": "text"},
                "publish_date": {"type": "date"},
                "has_video": {"type": "boolean"}
            }
        }
    }
    try:
        if not es_obj().indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es_obj().indices.create(index=index_name, ignore=400, body=settings)
            print(f'Created Index {index_name}')
        result = True
    except Exception as ex:
        print('Error while creating index: %s' % str(ex))
    finally:
        return result


def add_doc_to_index(index_name, document_data):
    is_stored = True
    try:
        response = es_obj().index(index=index_name, doc_type='_doc', body=json.dumps(document_data))
        print(response)
    except Exception as ex:
        print('Error in indexing data: %s' % str(ex))
        is_stored = False
    finally:
        return is_stored


def get_doc_from_index(index_name):
    response = None
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/full-text-queries.html
    search_object = {'query': {'match': {'website': 'smallintro.github.io'}}}
    search_data = json.dumps(search_object)
    try:
        response = es_obj().search(index=index_name, body=search_data)
        print(response)
    except Exception as ex:
        print('Error in indexing data: %s' % str(ex))
    finally:
        return response


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    _index_name = 'articles'
    article_data = {
        "author": "Sushil",
        "title": "Small intro to elasticsearch python API",
        "website": "smallintro.github.io",
        "publish_date": "2021-11-14",
        "has_video": True,
    }
    if init_elasticsearch:
        create_index(_index_name)
        add_doc_to_index(_index_name, article_data)
        get_doc_from_index(_index_name)
