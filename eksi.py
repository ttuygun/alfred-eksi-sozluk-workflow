#!/usr/bin/python
# encoding: iso-8859-1
import sys
import urllib
from workflow import Workflow, ICON_WEB, web
from unicodedata import normalize

base_url = "https://eksisozluk.com/"

def main(wf):
    headers = {'X-Requested-With': 'XMLHttpRequest'}

    args = wf.args
    query = urllib.quote_plus(args[0].encode('utf-8'))
    
    url = 'https://eksisozluk.com/autocomplete/query?q='+query
    r = web.get(url, headers=headers)
    r.raise_for_status()
    result = r.json()

    result = result['Titles']

    for q in result:
        wf.add_item(title=q, arg=base_url+q, valid=True)
    
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))