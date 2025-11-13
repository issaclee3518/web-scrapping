import requests
from bs4 import BeautifulSoup
url = "https://www.google.com"

response = requests.get(url)
html='''
<nav class="navbar">
    <div class="container">
        <a href="/" class="navbar-brand">My Website</a>
    </div>
</nav>
<main>
    <h1>Welcome to my website</h1>
    <div>This is a simple website built with HTML and CSS.</div>
    <a href="https://www.google.com">Google</a>
</main>
<footer>
    <div>Copyright 2025 My Website</div>
</footer>
'''
bs = BeautifulSoup(html,"html.parser")
print(response.status_code)

div_tags = bs.select('div')
print(div_tags)
for div_tag in div_tags:
    print(div_tag.get_text())
print("--------------------------------")
print(bs)