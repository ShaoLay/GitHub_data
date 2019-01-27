import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total resposerise:", response_dict['total_count'])   # 指出github包含多少个Python仓库
# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositorise returned:", len(repo_dicts))        #response_dict字典存储在列表中，列表里每个字典都包含有关一个Python仓库的信息
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)#创建条形图，让标签绕x轴旋转45度（x_label_rotation=45 ），隐藏图例（show_legend=False ）
chart.title = 'Most-Starred Python Projects on GitHub'#指定标题
chart.x_labels=names#横坐标标签
chart.add('',stars)#添加数据，标签设置成空字符串
chart.render_to_file('python_repos.svg')

