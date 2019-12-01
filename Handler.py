import os
import json
import requests

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

    open('output.txt', 'w').write(text)


def parse_text(results):
    text = ''
    try:
        for region in results['regions']:
            for line in region['lines']:
                for word in line['words']:
                    text += word['text'] + ' '
                text += '\n'
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

output = 55
Totalimages = 595
Accuracy = output*100/Totalimages
print(Accuracy)
#accuracy = 9.24