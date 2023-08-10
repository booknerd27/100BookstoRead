import requests
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/books/2015/aug/17/the-100-best-novels-written-in-english-the-full-list"
file = open("Books_To_Read.txt", "w")
file.write("")
file = open("Books_To_Read.txt","a")

r = requests.get(URL)
webpage = r.text
soup = BeautifulSoup(webpage, "html.parser")
i=1
for book in soup.select(" strong > a"):

    file.write(f"{i}){book.getText()}\n")
    i+=1
file.close()

with open("Books_To_Read.txt", "r") as file:
    book_list = file.read()


github_readme = f"""
# Books To Read

A list of some great books to read:

"""

# Write the README content to a file
with open("README.md", "w") as readme_file:
    readme_file.write(github_readme)
