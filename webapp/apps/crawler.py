import re

import validators
from newspaper import Article


def is_url(url):
    return validators.url(url)


def crawl(url):
    if not is_url(url):
        result = {
            'url': url,
            'error': 'Invalid Url',
            'success': False
        }

        return result
    article = Article(url)
    article.download()
    article.parse()
    result = {'url': url, 'error': '', 'success': True, 'title': article.title,
           'keywords': ', '.join(article.keywords if article.keywords else (
               article.meta_keywords if article.meta_keywords else article.meta_data.get('keywords', []))),
           'published_date': article.publish_date if article.publish_date
           else article.meta_data.get('pubdate', ''), 'top_img': article.top_image,
           'content': re.sub('\\n+', '</p><p>', '<p>' + article.text + '</p>')}
    return result


if __name__ == '__main__':
    res = crawl(
        'https://edition.cnn.com/2020/05/02/uk/princess-charlotte-fifth-birthday-intl-scli-gbr/index.html')
    print(res)