from bs4 import BeautifulSoup as bs
import requests


class SearchRepos:

    def find_url(self, url_str):
        '''
        Description: This function is used to match the word against the list of URLs scraped from the
        given website and return the matched URL.
        input: url_str- takes input string to be matched against the list of url
        output: url- returns the matched url against given the string
        '''
        if len(url_str) == 0 or len(url_str) == 1:
            return "Input string too short"

        url_list = []

        parent_url = "https://github.com/vinta/awesome-python"

        req = requests.get(parent_url)

        soup = bs(req.content, 'html.parser')

        for link in soup.find_all('a'):
            if "#" not in link.get('href') and link.get('href').startswith('https') \
                    and link.get('href') not in url_list:
                url_list.append(link.get('href'))
                # print(link.get('href'))

        for url in url_list:
            if url.find(url_str) != -1:
                return url

        return "No url exists with given input string"

sr = SearchRepos()
print("Query?")
input_str = input()
result = sr.find_url(input_str)
print(result)
# // <li><aa data-hydro-click>:originatinh_url
