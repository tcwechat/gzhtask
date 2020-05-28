


from requests import request
from loguru import logger

def follow_run(**kwargs):

    response = request(method="POST",url=kwargs.get('url'),json=kwargs.get("data"))

    logger.info(response.text)

def reply_run(**kwargs):

    response = request(method="POST",url=kwargs.get('url'),json=kwargs.get("data"))

    logger.info(response.text)