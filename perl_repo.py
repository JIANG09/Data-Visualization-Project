import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# implement API and store response
url = 'https://api.github.com/search/repositories?q=language:perl&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# keep API response in a variable
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# explore the info about repositories
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))


####print('\nSelected information about eachrepository:')
##for repo_dict in repo_dicts:
##    print('Name:', repo_dict['name'])
##    print('Owner:', repo_dict['owner']['login'])
##    print('Stars:', repo_dict['stargazers_count'])
##    print('Repository:', repo_dict['html_url'])
##    print('Created:', repo_dict['created_at'])
##    print('Updated:', repo_dict['updated_at'])
##    print('Watchers:', repo_dict['watchers_count'])        

names, plot_dicts= [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    if repo_dict['description']:
        desc = repo_dict['description']
    else:
        desc = 'No desciption provided.'
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': desc,
        'xlink': repo_dict['html_url']}
    
    plot_dicts.append(plot_dict)


# visualize
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Perl Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('perl_repos.svg')

    
     
    


