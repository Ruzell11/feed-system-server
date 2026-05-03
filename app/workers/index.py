from rq import SimpleWorker, Queue
from app.core.redis import redis_client

if __name__ == "__main__":
    queue = Queue("feed_queue", connection=redis_client)
    worker = SimpleWorker([queue], connection=redis_client)
    worker.work()