from tornado.web import url
from apps.task.api import *
from router import api_base_url,join_url

api_url = join_url(api_base_url,"/task")

urlpattern = [
    url(join_url(api_url, '/follow'), Follow),
    url(join_url(api_url, '/reply'), Reply),
    url(join_url(api_url, '/msgcustomer'), MsgCustomer),
    url(join_url(api_url, '/msgmould'), MsgMould),
    url(join_url(api_url, '/msgmass'), MsgMass),
]

print(api_url)