from flask import Flask, request, render_template

from crawler import crawl

app = Flask(__name__, template_folder='views')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('crawling_page.html')
    else:
        try:
            url = request.form['url']
            res = crawl(url)
            if res.get('error') != '':
                return render_template('crawling_page.html',
                                       error=res.get('error'))
            else:
                return render_template('crawling_page.html',
                                       title=res.get('title'),
                                       content=res.get('content'),
                                       url=res.get('url'),
                                       keywords=res.get('keywords'),
                                       published_date=res.get('published_date'),
                                       top_img=res.get('top_img'))
        except:
            return render_template('crawling_page.html', error='Try another url')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
