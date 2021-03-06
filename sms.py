import requests
from requests.auth import HTTPBasicAuth

def send_sms(sid, token, src, dest, text):
    """
    src and dest are str and need the country prefix like +30
    returns response in text form
    """
    host = 'https://tadhack.restcomm.com'
    endpoint = '/restcomm/2012-04-24/Accounts/' + sid + '/SMS/Messages.json'
    url = host + endpoint
    auth = (sid, token)
    body = {
        'To': dest,
        'From': src,
        'Body': text
    }
    response = requests.post(url, body, auth=auth)
    assert response.status_code==200
    r = response.json()
    assert 'status' in r.keys(), 'No status key in response body: ' + response.text
    assert r['status']=='sending', "Status is not 'sending' for response body:" + response.text
    return text

def main():
    sid = open('sid').read().strip()
    token = open('token').read().strip()
    src = open('msisdn_src').read().strip()
    dest = open('msisdn_dest').read().strip()
    print send_sms(sid, token, src, dest, 'SMS sent successfully...')

if __name__=='__main__':
    main()

