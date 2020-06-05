
import os

common=dict(
    gzip = 'on',
    debug = False,
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    port = 9887,
    serverurl = "http://localhost:9887",
    busiServer = "http://localhost:9888"
)
common['static'] = os.path.join(common['basedir'],"static")
common['images'] = os.path.join(common['static'],"images")

mysql=dict(
	host = 'localhost',
	port = 3306,
	user = 'root',
    name = "hdb",
	password = '!@#tc123',
    min_connections=2,
    max_connections=10,
    charset='utf8'
)

redis=dict(
    host='localhost',
    port=6379,
    password="123456",
    db = 0,
    minsize = 5,
    maxsize = 20,
    encoding = 'utf8'
)

config_insert=dict(
	common = common,
	mysql = mysql,
	redis = redis
)