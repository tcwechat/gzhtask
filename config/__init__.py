
import os

common=dict(
    gzip = 'on',
    debug = False,
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    port = int(os.getenv("PORT",8000)),
    busiServer = os.getenv("SERVERURL",None)
)
common['static'] = os.path.join(common['basedir'],"static")
common['images'] = os.path.join(common['static'],"images")

mysql=dict(
	host = os.getenv("DBHOST",None),
	port = int(os.getenv("DBPORT",3306)),
	user = os.getenv("DBUSER",None),
    name = os.getenv("DBNAME",None),
	password = os.getenv("DBPASS",None),
    min_connections=2,
    max_connections=10,
    charset='utf8mb4'
)

redis=dict(
    host=os.getenv("REDISHOST",None),
    port=int(os.getenv("REDISPORT",None)),
    password=os.getenv("REDISPASS",None),
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