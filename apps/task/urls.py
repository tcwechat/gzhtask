from tornado.web import url
from apps.task.api import *
from router import api_base_url,join_url

api_url = join_url(api_base_url,"/task")

urlpattern = [
    url(join_url(api_url, '/follow'), Follow),
]

print(api_url)