import redis

rserv = redis.Redis('localhost')

rserv.set('name', 'Adam')

name = rserv.get('name')

name.decode('UTF-8')