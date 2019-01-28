import random
import time

from prometheus_client import Counter
from prometheus_client import start_http_server, Summary

# Metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Metric to track number of calls made to process_request().
INVOKE_COUNTER = Counter('process_request_invoke_counter', 'Description of process_request_invoke_counter')


# A dummy function that takes some random amount of time.
# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    INVOKE_COUNTER.inc()
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)

    # Generate some requests.
    while True:
        process_request(random.random())
