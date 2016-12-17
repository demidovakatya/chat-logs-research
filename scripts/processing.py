import os
import re

folder = 'data'
raw_log_file = os.path.join(folder, 'log_dratuti.txt')
clean_log_file = os.path.join(folder, 'clean_log_dratuti.txt')

with open(raw_log_file) as lf:
    log = lf.readlines()
print(len(log))

text = ''.join(log)

# remove urls
regex_url = re.compile(r'https?://[^\s]*')
text = regex_url.sub(' ', text)

# remove mentions
regex_mention = re.compile(r'[^\w\d]?@[\w\d]+[^\w\d]')
text = regex_mention.sub(' ', text)

punctuation = '"#$%&\'()*+/:,-.?!;<=>@[\]^_`{|}~'
text = ''.join([ch for ch in text if not ch in punctuation])

text = text.lower()

with open(clean_log_file, 'w') as lf:
    lf.write(text)