import newspaper
import sys 

if len(sys.argv) != 2:
    print("Usage: python3 PythonNewspaper.py <url>")
    sys.exit(1)

url = sys.argv[1]

article = newspaper.Article(url)
article.download()
article.parse()

title = article.title.replace(" ", "_")

with open(f"{title}.txt", "w") as f:
    f.write(article.text)

print("Article saved as", title + ".txt")
