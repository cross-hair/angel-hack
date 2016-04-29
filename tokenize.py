import json
import re # import regex
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # get HTML tags
    r'(?:@[\w_]+)', # get @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # get hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # get URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', #  get numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", #  get words with - and '
    r'(?:[\w_]+)', #  get other words
    r'(?:\S)' #  get anything else
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
    try:
        with open('stream.json', 'r') as r:
            for line in r:
                tweet=json.loads(line)
                tokens=preprocess(tweet['text'])
                print(tokens)
 
def write(self, data):
    try:
        with open('stream.json', 'r') as r:
            for line in r:
                tweet=json.loads(line)
                tokens=preprocess(tweet['text'])
                with open('readable.json', 'a') as w:
                    w.write(tokens)
                    print(tokens)

if __name__ == '__main__':
    tokenize()
    preprocess()
    write()
