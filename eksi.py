#!/usr/bin/python
# encoding: utf-8
import sys
from workflow import Workflow, ICON_WEB, web

base_url = "https://eksisozluk.com/"

def main(wf):
    headers = {'Content-Type': 'application/json; charset=utf-8' ,'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36', 'X-Requested-With': 'XMLHttpRequest'}

    if len(wf.args):
        query = wf.args[0]
        query = query.replace(" ", "%20")
    else:
        query = None

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