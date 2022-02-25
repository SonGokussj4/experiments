from datetime import datetime
import time

def get_url(url):
    print(f'')
    print(f'Getting {url} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')
    time.sleep(0.5)
    return url
