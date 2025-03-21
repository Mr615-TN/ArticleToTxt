import newspaper

article = newspaper.Article("https://www.42rulesforlife.com/why-i-am-not-a-pacifist")
article.download()
article.parse()
print(article.text)
