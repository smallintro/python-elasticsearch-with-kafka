"""
Created on 14-Nov-2021
@author: Sushil Prasad
"""
import logging
import uvicorn
import threading
from service.kafka_consumer import consume_message


def init_app():
    logging.basicConfig(level=logging.ERROR)
    try:
        threading.Thread(target=consume_message).start()
        print('Hello World!')
    except Exception as ex:
        print(str(ex))


if __name__ == "__main__":
    init_app()
    # uvicorn article_api:app --port 8080 --reload
    uvicorn.run("article_api:app_v1", host="127.0.0.1", port=8080, log_level="info")
