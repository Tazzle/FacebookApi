import urllib
import json

    username = USER_ID
    photo_limit = 1000
    access_token = USER_ACCESS_TOKEN

    uri = "https://graph.facebook.com/%s/photos?type=tagged&limit=%s&access_token=%s" % (username, photo_limit, access_token)
    
    #encode
    url = urllib.quote(uri).encode('utf8')

    #urrlib.urlopen returns a file-like object, to return as string use read()
    resultset = urllib.urlopen(uri).read()
 
    #testing - printing resulset as prettified json
    photoData = open('JSONOutput.json', 'w')
    photoData.write(json.dumps(json.loads(resultset), sort_keys=False, indent=4, separators=(',', ': ')))
    photoData.close()
    
    #testing - walking through the nested items
    resultset = json.loads(resultset)

    #test
    resultset['data'][0]['images'][3]['source']

    #test
    for images in resultset['data'][0]['images']:
        print images['width']
        if images['width'] == 800:
            print images['source']
            
    #test
    print len(resultset['data'])
   








   