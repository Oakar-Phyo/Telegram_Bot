import requests 
import time
msg =['Hey Man','What Up!','Everything is ok right?','My name is Ryan']

for send in msg:
  url = 'https://api.telegram.org/bot5982639798:AAGlm4LMOvt6zYb9cBuWRE11XRT5B-X_IOQ/sendMessage?chat_id=-1001639787748&text={}'.format(send)
  requests.get(url)
  time.sleep(15)
 