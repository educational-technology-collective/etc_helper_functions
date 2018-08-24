import requests
import validators

def read_html(url):
    if validators.url(url):
        '''
        Make a get call to the proxy server
        '''
        r = requests.get('http://proxy.mentoracademy.org/readHtml/?url=' + url)
        return r.content
    else:
        return "Please use a valid url!"