import requests 
import time

token = your token
groupid = yourgroupid
msg =['Hey Man','What Up!','Everything is ok right?','My name is Ryan']

for send in msg:
  url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={groupid}&text={send}'
  requests.get(url)
  time.sleep(15)
 
