#!/usr/bin/python

import bottle
import requests
import json, pprint


app = application = bottle.Bottle()


@app.route('/page/template')
@bottle.view('template.tpl')
def show_page():

    return dict(name='Hamdy2')


@app.route('/')
def show_index():
    '''
    The front "index" page
    '''
    result = gh_search_repository('arrow')
    return result

@app.route('/navigator')
def navigator():
    search_term = bottle.request.query.search_term
    if(search_term):
        items = gh_search_repository(search_term)
        lstRepoModel=[]
        prepare_model(items, lstRepoModel)
        return bottle.template( 'template.tpl',search_term=search_term, model= lstRepoModel)
    else:
        return 'please enter saerch term'

def prepare_model(repos, lstRepoModel):
    for item in repos:
        repoModel = {}
        repoModel['respository_name'] = item['full_name']
        repoModel['created_at'] = item['created_at']
        repoModel['owner_url'] = item['owner']['url']
        repoModel['avatar_url'] = item['owner']['avatar_url']
        repoModel['owner_login'] = item['owner']['login']
        lastCommit = gh_last_commits(item['full_name'])
        repoModel['commit_message'] = lastCommit['commit']['message']
        repoModel['commit_author_name'] = lastCommit['commit']['author']['name']
        lstRepoModel.append(repoModel)
    return

def gh_search_repository(search_term,page_size=5, url='https://api.github.com/search/repositories'):
    query = url + '?q=%s' % search_term
    data = callAPI(query)
    repos = data['items']
    repos = sorted(repos, key=lambda repo: repo['created_at'], reverse=True)
    return repos[:page_size]

def gh_last_commits(repoName, url='eee'):
    url = 'https://api.github.com/repos/%s/commits'
    data = callAPI(url % repoName)
    commit = data[0]
    #repo['lastCommit']['commit_message'] = commit[0]['commit']['message']
    #repo['lastCommit']['commit_author_name'] = commit[0]['commit']['author']['name']
    return commit

def callAPI(url):
    result = requests.get(url)
    if (result.ok):
        repoItem = json.loads(result.text or result.content)
        return repoItem
    return 'Error'



app.run(host='localhost', port=8080)
