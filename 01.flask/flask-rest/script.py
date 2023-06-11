from time import time
from requests import post

headers =  {'Content-Type': 'application/json; charset=utf-8'}

def wait_process(contract_data, thread_value):
    start_time = time()
    # print(contract_data)
    while True:
        current_time = time()
        if current_time - start_time > 5:
            break
    
    res = post("http://127.0.0.1:6000", headers=headers, json={"message": "selenium bot çalıştı ve şu sonucu döndü..."})
    print(res.json())
    thread_value.append("hi")
    return


# URL = 'https://google.com/'
# headers =  {'Content-Type': 'application/json; charset=utf-8'}
# body = {
#     'username': 'linuxhint',
#     'password': 'pasword'
# }
# resp = requests.post(url=URL, headers=headers, json=body)
# print(resp.json())