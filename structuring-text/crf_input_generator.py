import sys
import nltk
import json


for line in sys.stdin:
    data = json.loads(line)
    for ingredient in data['ingredients']:
        tokens = nltk.word_tokenize(ingredient.strip())
        tagged_tokens = nltk.pos_tag(tokens)
        for token, pos in tagged_tokens:
            try:
                print "%s\t%s" % (token.encode('utf8'), pos)
            except:
                print "Error writing token:", token
