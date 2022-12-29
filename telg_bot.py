import requests
from datetime import datetime
import pytz

ryan = pytz.timezone('Asia/Myanmar')
raw_TS = datetime.now(ryan)
curr_date = raw_TS.strftime("%d-%m-%Y")
curr_time = raw_TS.strftime("%H:%M:%S")

telg_token = "5982639798:AAGlm4LMOvt6zYb9cBuWRE11XRT5B-X_IOQ"
telg_groupid = "-1001639787748"

msg = f"Hey Man! {curr_date} at {curr_time} "

def sendmgs_telg(message):
    telg_api = f"https://api.telegram.org/bot{telg_token}/sendMessage?chat_id=@{telg_groupid}&text={message}"
    tel_rep = requests.get(telg_api)

    if tel_rep.status_code == 200:
        print("INFO : Hey Man!")

    else:
        print("Error : Colud not send!")

        sendmgs_telg(msg)

