
from requests import request
from loguru import logger
from config import config_insert


def AccCount():

    print(config_insert['common'])

    response = request(method="POST",url="{}/v1/api/wechat/AccCount_Handler".format(config_insert['common'].get("busiServer")),json={"data":{}})

    logger.info(response.text)
