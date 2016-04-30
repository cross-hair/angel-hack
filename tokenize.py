import json
import re
import operator 
import json
from collections import Counter

 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # get HTML tags
    r'(?:@[\w_]+)', #  get @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # get hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', #  get numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # get  words with - and '
    r'(?:[\w_]+)', #  get other words
    r'(?:\S)' # get anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
def frequency(self, data):
    fname = 'stream.json'
    with open(fname, 'r') as f:
        count_all = Counter()
        for line in f:
            tweet = json.loads(line)
            terms_all = [term for term in preprocess(tweet['text'])]
            count_all.update(terms_all)
            #print(count_all.most_common(100))
            try:
                with open('readable.json', 'a') as f:
                    data = ''.join(terms_all)
                    f.write(data)
                    #print(data)
                    return True
            except BaseException as e:
                print("Error on_data: %s" % str(e))
            return True

def template(self, data):
    fname = 'stream.json'
    with open(fname, 'r') as f:
        data = {
        "type": "crosshair",
        "mark": []
        }
        for line in f:
            tweet = json.loads(line)
            if tweet['coordinates']:
                geo_json_feature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }}
                data['mark'].append(geo_json_feature)
                with open('data.json', 'w') as f:
                    f.write(json.dumps(data, indent=4))
if __name__ == '__main__':
    tokenize('s')
    preprocess('s', 's')
    frequency('s', 's')
    template('s', 's')

