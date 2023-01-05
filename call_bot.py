import requests 

# Token =your token
# groupid = your groupid

msg =['Hey Man! This is Assistant calling to you to inform you about something that is happening at your house']

for send in msg:
  
#   call_url = f'https://api.callmebot.com/start.php?chat_id={groupid}&text={send}'
#   sms = f'https://api.callmebot.com/signal/send.php?chat_id={groupid}&apikey={Token}&text={send}'

  call = f'http://api.callmebot.com/start.php?source=HA&user=@oakarphyoe&text={send}&lang=en-GB-Standard-B'
  requests.get(call)
  print(send)

 
