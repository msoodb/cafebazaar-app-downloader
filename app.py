import sys
import json
import requests

pkg = sys.argv[1]
sdk="22"
cpu="x86,armeabi-v7a,armeabi"

try:
    url = f"https://api.cafebazaar.ir/rest-v1/process/AppDetailsV2Request"
    headers = {
        'accept': "application/json",
        "Content-Type": "application/json; charset=utf-8"
    }
    body = {
            "properties":{
                "language":2,
                "clientID":"k8gehx0szc0m9ooa0owdiwuo46wjrkdk",
                "deviceID":"k8gehx0szc0m9ooa0owdiwuo46wjrkdk",
                "clientVersion":"web"
            },
            "singleRequest":{
                "appDetailsV2Request":{
                    "packageName":pkg
                }
            }
        }    
    response = requests.request("POST", url, headers=headers, data=json.dumps(body))
    with open(f"{pkg}Details.json", 'w') as f:
        f.write(json.dumps(response.json(), indent=4))
        f.close()

    url = f"https://api.cafebazaar.ir/rest-v1/process/AppDownloadInfoRequest"
    headers = {
        'accept': "application/json",
        "Content-Type": "application/json; charset=utf-8"
    }
    body = {            
        "properties": {
            "language": 2,
            "clientVersionCode": 1100301,
            "androidClientInfo": {
              "sdkVersion": 22,
              "cpu": "x86,armeabi-v7a,armeabi",
            },
            "clientVersion": "11.3.1",
            "isKidsEnabled": False,
          },
          "singleRequest": {
            "appDownloadInfoRequest": {
              "downloadStatus": 1,
              "packageName": pkg,
              "referrers": [],
            },
          },
        }
    response = requests.request("POST", url, headers=headers, data=json.dumps(body))
    with open(f"{pkg}DownloadInfo.json", 'w') as f:
        f.write(json.dumps(response.json(), indent=4))
        f.close()

    token = response.json().get("singleReply").get("appDownloadInfoReply").get("token")
    cdnPrefix = response.json().get("singleReply").get("appDownloadInfoReply").get("cdnPrefix")[0]
    downloadLink = f"{cdnPrefix}apks/{token}.apk"

    print (downloadLink)
    with open(f"downloadLinks.txt", 'a') as f:
        f.write(downloadLink)
        f.write('\n')
        f.close()

except:
    print("error!")