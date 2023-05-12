import random
import requests
import time

while True:
    n = random.choice([0, 5, 10, 15, 20, 25, 91])
    try:
        print(requests.get(f"http://fibonacci:80/fibonacci?n={n}"))
    except requests.exceptions.ConnectionError as ce:
        print(ce)

    time.sleep(5)
