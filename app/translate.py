# __author__ = 'hd'

try:
    import httplib  # Python 2
except ImportError:
    import http.client as httplib  # Python 3
try:
    from urllib import urlencode  # Python 2
except ImportError:
    from urllib.parse import urlencode  # Python 3
import json
from flask.ext.babel import gettext
from config import MS_TRANSLATOR_CLIENT_ID, MS_TRANSLATOR_CLIENT_SECRET


def microsoft_translate(text, source_lang, dest_lang):
    if MS_TRANSLATOR_CLIENT_ID == "" or MS_TRANSLATOR_CLIENT_SECRET == "":
        return gettext('Error: translation service not configured.')

    # get access token
    params = urlencode({
        'client_id': MS_TRANSLATOR_CLIENT_ID,
        'client_secret': MS_TRANSLATOR_CLIENT_SECRET,
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'})
    conn = httplib.HTTPSConnection("datamarket.accesscontrol.windows.net")
    conn.request("POST", "/v2/OAuth2-13", params)
    raw_response = conn.getresponse().read()
    response = json.loads(raw_response)
    token = response[u'access_token']

    # translate
    conn = httplib.HTTPConnection('api.microsofttranslator.com')
    params = urlencode({'appId': '',
                        'from': source_lang,
                        'to': dest_lang,
                        'text': text.encode("utf-8")})
    url = '/V2/Ajax.svc/Translate?' + params
    header = {'Authorization': 'Bearer ' + token}
    conn.request("GET", url, headers=header)
    raw_response = conn.getresponse().read().decode('utf-8').replace(u'\ufeff', '')
    raw_response = "{\"response\":" + raw_response + "}"
    response = json.loads(raw_response)
    return response["response"]