import time

requests = {}

LIMIT = 10
TIME_WINDOW = 10

def check_request(ip):
    current_time = time.time()

    if ip not in requests:
        requests[ip] = []

    requests[ip] = [t for t in requests[ip] if current_time - t < TIME_WINDOW]

    requests[ip].append(current_time)

    if len(requests[ip]) > LIMIT:
        return True

    return False