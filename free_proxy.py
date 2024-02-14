from requests import session
from datetime import datetime



class FreeProxyServer:
    def __init__(self) -> None:
        pass


    def __makeSession(self):
        headers = {
            'authority': 'checkerproxy.net',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': '_ga=GA1.2.188275493.1698807492; _gid=GA1.2.810646382.1698807492; _gat=1',
            'referer': 'https://checkerproxy.net/archive/2023-11-01',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        }
        sess = session()
        sess.headers.update(headers)
        return sess

    def __getProxyData(self,sess):
        archiveDate = datetime.now().strftime("%Y-%m-%d") #'2023-11-01'
        API_URL = f'https://checkerproxy.net/api/archive/{archiveDate}'
        resp = sess.get(API_URL)
        if resp.status_code == 200:
            jsonResp = resp.json()
            if jsonResp:
                proxyData = jsonResp
            else:
                proxyData = []
        return proxyData

    def getWorkingProxies(self,proxy_type='http'):
        if proxy_type not in ['http', 'https']: return {'errorMsg':'Proxy Type is Invalid'}
        # proxyTypeNum 1 mean HTTP and 2 mean HTTPS
        proxyTypeNum = 1 if proxy_type == 'http' else 2
        sess = self.__makeSession()
        proxyData =  self.__getProxyData(sess)
        workingProxyList = []
        for item in proxyData:
            proxyAddress = item.get('addr')
            proxyType = item.get('type')
            timeout = item.get('timeout')
            if proxyType == proxyTypeNum and timeout <= 5000: # 5000ms == 5 seconds
                workingProxyList.append(proxyAddress)
        return workingProxyList
    

if __name__ == '__main__':
    proxyServer = FreeProxyServer()
    proxies = proxyServer.getWorkingProxies()
    print(len(proxies), 'Proxies Found ...')
    print(proxies)