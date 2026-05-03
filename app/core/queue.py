from rq import Queue
from app.core.redis import redis_client

feed_queue = Queue("feed_queue", connection=redis_client)