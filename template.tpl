<!DOCTYPE html>
<html>
<head>
    <title>Github Navigator</title>
</head>
<body>

<h1>{{search_term}}</h1>

<ul>
  % for i, repo in enumerate(model):
    <h2>{{i+1}}. {{repo['respository_name']}}</h2>
    <h3> Created {{repo['created_at']}}</h3>
    <a href="{{repo['owner_url']}}"><img src="{{repo['avatar_url']}}" alt="avatar" height="42" width="42"/></a>
    {{repo['owner_login']}}
    <h3>LastCommit</h3>
    {sha} {{repo['commit_message']}}  {{repo['commit_author_name']}}
    <hr/>
  % end
</ul>

</body>
</html>