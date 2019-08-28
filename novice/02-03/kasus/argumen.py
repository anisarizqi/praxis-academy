
import concurrent.futures
import requests
import threading
import time
import argparse



parser = argparse.ArgumentParser()

parser.add_argument( "-u" , "--url", 
						type = str,
						required = True,
						help = 'masukkan url'
						)
args = vars(parser.parse_args())

threadLocal = threading.local()

def get_session():
	if not hasattr(threadLocal, 'session'):
		threadLocal.session = requests.Session()
	return threadLocal.session

def download_site(url):
	session = get_session()
	with session.get(url) as response:
		print(f'Read {len(response.content)} from {url}')

def download_all_sites(sites):
	with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
		executor.map(download_site, sites)

if __name__ == "__main__":

    sites = [
    args["url"]
    ] * 20
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")