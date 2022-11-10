import requests

r= requests.get('https://quotes.toscrape.com')

# r.status_code
# r.encoding
# r.text

html = r.text.split('\n')

with open('authors.txt', 'w') as file :
  for line in html :
    # print(line)
    if '<span>by <small class="author" itemprop="author">' in line :
      author = str(line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','').strip())
      file.write(author)
      print(author)
      file.write('\n')



