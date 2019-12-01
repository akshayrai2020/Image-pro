import os
import json
import requests
import datetime

API_KEY = 'API KEY'
ENDPOINT = 'API END POINT'
DIR = 'IMAGE PATH'


def handler():
    text = ''
    for filename in sorted(os.listdir(DIR)):
        if filename.endswith(".jpeg"):
            pathToImage = '{0}/{1}'.format(DIR, filename)
            results = get_text(pathToImage)
            text += parse_text(results)

    open('output1.txt', 'w').write(text)


def parse_text(results):
    # print(results)
    count = 0
    text = ''
    try:

        for lines in results['regions'][0]['lines']:
            for word in lines['words']:
                temp = word['text']
                # print(temp)
                if "2019" in temp or "19" in temp or count == 1 or "2018" in temp or "/" in temp or "-" in temp:
                    text += temp
                    text += '\n'
                if temp in 'Date':
                    count = 1

    except:
        pass
    return text


def get_text(pathToImage):
    print('Processing: ' + pathToImage)
    headers = {
        'Ocp-Apim-Subscription-Key': API_KEY,
        'Content-Type': 'application/octet-stream'
    }
    params = {
        'language': 'en',
        'detectOrientation ': 'true'
    }
    payload = open(pathToImage, 'rb').read()
    response = requests.post(ENDPOINT, headers=headers,
                             params=params, data=payload)
    results = json.loads(response.content)
    return results


if __name__ == '__main__':
    handler()

output = 23
Totalimages = 595
Accuracy = output*100/Totalimages
print(Accuracy)
#accuracy = 3.86
