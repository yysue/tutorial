# -*- coding: utf-8 -*-

import os, urllib

articles = list()

def getinfo(file_path):
    res_data = {}
    res_data['file_path'] = file_path
    with open(file_path) as f:
        count = 0
        for line in f.readlines():
            line = line.strip()
            if line == '---':
                count = count + 1
                continue
            if count == 2:
                break
            if count == 0:
                continue
            arr = line.split(": ")
            res_data[arr[0].strip()] = arr[1].strip().lstrip('"').rstrip('"')
        if not res_data.has_key('title'):
            res_data['title'] = os.path.basename(file_path)
        if not res_data.has_key('date'):
            res_data['date'] = '2012-07-18 08:21:49'
    return res_data

def get_articles(dir_path):
    dirs = os.listdir(dir_path)
    for filename in dirs:
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            suffix = os.path.splitext(filename)[1]
            if '.md' != suffix:
                continue
            article = getinfo(file_path)
            articles.append(article)
        else:
            get_articles(file_path)

#dir_path = r'E:\git_home\tutorial\contents'
dir_path = 'contents'
get_articles(dir_path)

def article_cmp(x, y):
    if x['date'] > y['date']:
        return -1
    return 1

#sorted(articles, cmp=article_cmp)

# 路径 标题 日期 分类 标签
article_dict = dict()
for article in articles:
    article_date = article['date']
    article_ym = article_date[:7]
    if not article_dict.has_key(article_ym):
        article_dict[article_ym] = list()
    article_dict[article_ym].append(article)
# article_date.md
# article_tag.md
# article_category.md
fout = open('README.md', 'w')
for (k, v) in article_dict.items():
    fout.write('# %s\n\n' % k)
    sorted(v, cmp=article_cmp)
    for article in v:
        title = article['date'][:10] + '-' + article['title']
        if k == '2012-07':
            title = article['title']
        url = article['file_path'].replace(dir_path, 'contents')
        url = urllib.pathname2url(url)
        fout.write('[%s](%s)\n\n' % (title, url))
    



