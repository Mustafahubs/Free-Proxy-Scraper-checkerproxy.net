# Free Proxy Server Checker

This Python script allows you to check and retrieve a list of working free proxy servers from the internet. It utilizes the checkerproxy.net API to fetch proxy data and filter out working proxies based on specified criteria.

## Features

- Retrieves working free proxy servers from checkerproxy.net API.
- Supports filtering proxies based on HTTP or HTTPS protocol.
- Checks the response time of each proxy and filters out proxies with response times greater than 5 seconds.
- Provides a simple interface to integrate proxy functionality into your Python applications.

## Usage

1. Clone the repository or download the script `free_proxy_server.py`.
2. Ensure you have `requests` library installed. You can install it via pip:

    ```
    pip install requests
    ```

3. Import the `FreeProxyServer` class from the script and create an instance.
4. Call the `getWorkingProxies()` method to retrieve a list of working proxies.
5. Optionally specify the proxy type (either 'http' or 'https').

```python
from free_proxy_server import FreeProxyServer

# Create an instance of FreeProxyServer
proxyServer = FreeProxyServer()

# Get a list of working proxies (default proxy type is HTTP)
proxies = proxyServer.getWorkingProxies()

# Alternatively, specify proxy type as 'https'
# proxies = proxyServer.getWorkingProxies(proxy_type='https')

print(len(proxies), 'Proxies Found ...')
print(proxies)
