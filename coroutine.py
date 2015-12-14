"""
Fetch the first ten characters of the pages defined in the sites list using the
requests (sync) library and aiohttp (async) library.

Show how to do it synchronously and asynchronously with the new async/await
syntax. Finally, compare runtimes of both methods.
"""
from time import time
from requests import get
from aiohttp import request
from asyncio import get_event_loop, wait

sites = [
    'https://www.google.com',
    'https://www.yahoo.com',
    'https://www.bbc.co.uk',
    'https://en.wikipedia.org',
    'https://de.wikipedia.org',
    'https://news.ycombinator.com',
    'https://www.tagesschau.de',
]

# Synchronous example
def get_site_snippet(site):
    response = get(site)
    return response.content[:10]

def main():
    # Iterate over URLs and print HTTP request results
    for site in sites:
        print(get_site_snippet(site))

# Asynchronous example
async def async_get_site_snippet(site):
    response = await request('GET', site)
    body = await response.read_and_close()
    return body[:10]

def async_main():
    # Create coroutine objects to be executed
    tasks = [async_get_site_snippet(site) for site in sites]
    loop = get_event_loop()

    # asyncio.wait bundles up all coroutine objects and waits for their
    # completion. This resembles a traditional thread queue join.
    task_bundle = wait(tasks)
    # run_until_complete will result a result and a pending set, we can discard
    # the latter.
    result, _ = loop.run_until_complete(task_bundle)
    loop.close()

    # Retrieve and print results
    for task in result:
        print(task.result())


if __name__ == "__main__":
    print("Running synchronous example")
    start = time()
    main()
    duration = time() - start

    print("Running asynchronous example")
    async_start = time()
    async_main()
    async_duration = time() - async_start

    print("Synchronous example took {} seconds".format(duration))
    print("Asynchronous example took {} seconds".format(async_duration))
