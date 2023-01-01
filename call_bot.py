import requests 
# import time
Token = '5982639798:AAGlm4LMOvt6zYb9cBuWRE11XRT5B-X_IOQ'
groupid = "-1001639787748"
msg =['Hey Man! This is Assistant calling to you to inform you about something that is happening at your house']

for send in msg:
  call_url = 'https://api.callmebot.com/start.php?chat_id={}&text={}'.format(groupid ,send)
  sms = f'https://api.callmebot.com/signal/send.php?chat_id={groupid}&apikey={Token}&text={send}'
  call = 'http://api.callmebot.com/start.php?source=HA&chat_id=-1001639787748&text={}&lang=en-GB-Standard-B'.format(send)
  url = 'https://api.telegram.org/bot5982639798:AAGlm4LMOvt6zYb9cBuWRE11XRT5B-X_IOQ/sendMessage?chat_id=-1001639787748&text={}'.format(send)
  requests.get(sms)
  print(send)

#   time.sleep(15)
 