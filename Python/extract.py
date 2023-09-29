from bs4 import BeautifulSoup
import requests

# url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
url='https://www.youtube.com/watch?v=eSCV-_VkE2c'

### Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

### Parse the html content
soup = BeautifulSoup(html_content, 'html.parser')
print(type(soup.html)) # print the parsed data of html
print(type(soup.prettify('utf-8')))
print(soup.title)
""" try:
  print(str(soup.prettify('utf-8').replace('\\n', '\n'))) # print the parsed data of html
except UnicodeEncodeError:
  print('something went wrong') """

### 'prettify()' method of a BeautifulSoup object returns a <str> type, but it's encoded in Unicode. You'll have issues if attempting to redirect this output to a file.
### Instead, to redirect this output to a file, feed an anternative encoding as a parameter for 'prettify()', force convert to str then replace the '\\n' ('\n' character) occurencies to '\n' (actual line breaks).
f = open("out.txt", "w")
try:
  f.write(str(soup.prettify('utf-8')).replace('\\n','\n'))
  print('Written to file.')
except UnicodeEncodeError:
  print('something went wrong')
f.close()