
# number of records per page
NR_PER_PAGE = 20

# how many pagination
PAGINATION = 5

MONGO_DB = {
    'host': '192.168.59.103',
    'port': 27017,
    'dbs': ['jobs']
}

PROTOBUF_SERVER = {'host': 'localhost', 'listen_port': 55001}

LOOPBACK = 'localhost'
SERVER_CONF = {'loopback': LOOPBACK, 'all': '0.0.0.0', 'listen_port': 8888, 'host': 'localhost'}

DEBUG = True