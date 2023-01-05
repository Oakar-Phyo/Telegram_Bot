import requests 
import time

token = your token
groupid= your groupid
msg =['Hey Man','What Up!','Are you ok?']

for send in msg:
  url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={groupid}&text={send}'
  requests.get(url)
  time.sleep(15)
  print (send)
 
