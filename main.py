import webbrowser
import sys

url = "https://www.google.com/search?q="

valid_websites = [
    'reddit.com',
    'medium.com',
    'google.com',
    'medium.com',
    'stackoverflow.com'
]

chrome_path = '/usr/bin/brave-browser --no-sandbox  %s'

def create_filter():
    filter ='('
    for index, website in enumerate(valid_websites):
        filter += 'site:' +website
        if index == len(valid_websites) -1:
            filter += ')'
        else:
            filter += ' OR '
    return filter

def create_query():
    query = sys.argv[1:]
    return ' '.join(query)

def create_url():
    if len(sys.argv[1:]) == 0:
        print('\nOpsss: navalidno tyrsene\n')
    else:
        final_url = url + create_query() + create_filter() 
        webbrowser.get(chrome_path).open(final_url)

create_url() 
