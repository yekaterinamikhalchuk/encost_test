
import requests
from bs4 import BeautifulSoup
import json

from celery import shared_task
from .models import News

@shared_task
def hackernews_rss():
    url_links = ['https://yandex.ru', 'https://www.djangoproject.com', 'https://www.python.org']
    article_list = []
    try:
        for url in url_links:
            print('Starting the Scrapping tool')
            # r = requests.get(f'https://api.domainsdb.info/v1/domains/search?domain={url}')
            r = requests.get(url)
            soup = BeautifulSoup(r.content, features='lxml')
            container = soup.findAll('a')
            url_storage = []
            for block in container:
                try:
                    url = block.get('href')
                    if url.startswith('http'):
                        url_storage.append(block.get('href'))
                except:
                    continue
            # "найденный url", "domain", "create_date", "update_date", "country", "isDead", "A", "NS", "CNAME", "MX", "TXT"
            for link in url_storage:
                r = requests.get(f'https://api.domainsdb.info/v1/domains/search?domain={link}')
                data = r.text
                parse_json = json.loads(data)
                for block in parse_json['domains']:
                    domain = block['domain']
                    create_date = block['create_date']
                    update_date = block['update_date']
                    country = block['country']
                    is_dead = block['isDead']
                    a = block['A']
                    ns = block['NS']
                    cname = block['CNAME']
                    mx = block['MX']
                    txt = block['TXT']
                    article = {
                        'domain': domain,
                        'link': link,
                        'create_date': create_date,
                        'update_date': update_date,
                        'country': country,
                        'is_dead': is_dead,
                        'a': a,
                        'ns': ns,
                        'cname': cname,
                        'mx': mx,
                        'txt': txt
                    }
                    article_list.append(article)
                print('Finished scraping the articles')

                # после цикла передаем сохраненный объект в файл .txt
                return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)


@shared_task(serializer='json')
def save_function(article_list):
    print('starting')
    new_count = 0

    for article in article_list:
        try:
            News.objects.create(
                domain=article['domain'],
                create_date = article['create_date'],
                update_date = article['update_date'],
                country = article['country'],
                is_dead = article['isDead'],
                a = article['A'],
                ns = article['NS'],
                cname = article['CNAME'],
                mx = article['MX'],
                txt = article['txt'],
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')