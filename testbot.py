import requests

token = "5982639798:AAGlm4LMOvt6zYb9cBuWRE11XRT5B-X_IOQ"
groupid = "-1001639787748"


url ='https://api.telegram.org/bot{}/getUpdates'.format(token)
resp = requests.get(url)
data = resp.json()

# msg = data["message"]["text"]

# def sendmgs_telg(message):

#   url ='https://api.telegram.org/bot{}/getUpdates'.format(token)
#   resp = requests.get(url)
#   data = resp.json()

#     # telg_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id=@{groupid}&text={message}"
#     #    resp = requests.get(telg_url)

#   if data["message"]["entities"][0]["type"] == "mention":
#            chat_id = data["message"]["chat"]["id"]
#            user_id = data["message"]["from"]["id"]
#            user_name = data["message"]["from"]["username"]
#            msg = data["message"]["text"]

#   elif 'Hi' in msg:
#         text=f'Hey Man {user_id}{user_name} What Up!'
#         tel_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
#         resp = requests.get(tel_url)

#   else:
#         print("Error : Colud not send!")

#         sendmgs_telg(text)
# print(resp.text)

for item in data["result"]:
        try:

            if item["message"]["entities"][0]["type"] == "mention":
                print(item)

                chat_id = item["message"]["chat"]["id"]
                user_id = item["message"]["from"]["id"]
                user_name = item["message"]["from"]["username"]
                message = item["message"]["text"]
                   

            if "Hi" in message.lower():
                 
                text= "Hey Man!"
                # text = '"<a href="tg://user?id={}">@{}</a> Hi, What Up! ,Do let me know if you need any help"'.format(user_id,user_name)
                go_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={groupid}&text={text}'
                resp = requests.get(go_url)
               

            else:
              print("Error : Colud not send!")
            
        except:
            print("Error!")

print("Program end")



