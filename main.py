import requests
from config.Config import Config


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


watsonConfig = Config.Instance().getWatsonConfig()
url = watsonConfig["url"]
user = watsonConfig["user"]
password = watsonConfig["password"]
dialogIdFile = open('dialog_id.txt', 'r')
dialogId = dialogIdFile.readline()
dialogIdFile.close()

resp = requests.post(url + "/v1/dialogs/" + dialogId + "/conversation", data={
    "input": ""
}, auth=(user, password))

jsonResp = resp.json()
clientId = jsonResp["client_id"]
conversationId = jsonResp["conversation_id"]
print ''
print bcolors.WARNING + "Watson: " + bcolors.OKBLUE + "\n".join(jsonResp["response"]) + bcolors.ENDC

while True:
    userResponse = raw_input(bcolors.WARNING + "You: " + bcolors.OKGREEN)
    resp = requests.post(url + "/v1/dialogs/" + dialogId + "/conversation", data={
        "client_id": clientId,
        "conversation_id": conversationId,
        "input": userResponse
    }, auth=(user, password))
    jsonResp = resp.json()
    print bcolors.WARNING + "Watson: " + bcolors.OKBLUE + "\n".join(jsonResp["response"]) + bcolors.ENDC
    if userResponse == "bye":
        break
