from elasticsearch import Elasticsearch
import requests

_es_obj = None
default_index = 'articles'


def init_elasticsearch():
    global _es_obj
    _es_obj = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es_obj.ping():
        print('Elasticsearch Connected')
        res = requests.get('http://localhost:9200')
        print(res.content)
        create_index()
        return True
    else:
        print('Elasticsearch not connected')
        return False


def es_obj():
    global _es_obj
    if _es_obj is None:
        init_elasticsearch()
    return _es_obj


def create_index(index_name=default_index):
    result = False
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
        else:
            es_obj().indices.refresh(index=index_name)
        result = True
    except Exception as ex:
        print('Error while creating index: %s' % str(ex))
    finally:
        return result

