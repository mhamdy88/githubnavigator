#!/usr/bin/python

import bottle
import requests
import json, pprint


app = application = bottle.Bottle()

@app.route('/')
def show_index():
    '''
    The front "index" page
    '''
    result = gh_search_repository('arrow')
    return result

@app.route('/page/template')
@bottle.view('template.tpl')
def show_page():

    return dict(name='Hamdy2')


def gh_search_repository(search_term, url='https://api.github.com/search/repositories'):
    query = url + '?q=%s' % search_term
    repos = callAPI(query)
    return json.dumps(repos, indent=2)


def gh_list_commits(url):

    return

def callAPI(url):
    result = requests.get(url)
    if (result.ok):
        repoItem = json.loads(result.text or result.content)
        return repoItem
    return 'Error'



app.run(host='localhost', port=8080)
