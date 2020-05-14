import webbrowser
text = 'search google for foxes '
keyword = 'search google for '

splicer = (text.find(keyword))
search_term = (text[splicer+len(keyword):])


search = 'https://www.google.com/search?q=' + search_term
webbrowser.open(search)


'''

from selenium import webdriver
import webbrowser

# prepare the option for the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('headless')

# start chrome browser
browser = webdriver.Chrome(chrome_options=options)
browser.get('http://www.google.com/xhtml')
print(browser.current_url)
webbrowser.open(browser.current_url)
browser.quit()
'''














'''
import time 
run = input("Start? > ")
mins = 0
# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 20 minutes running
    while mins != 20:
        print(">>>>>>>>>>>>>>>>>>>>> {}".format(mins))
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1
    # Bring up the dialog box here
'''




'''
import requests
import webbrowser
import bs4

content = 'how to make pie'
search = requests.get('https://www.google.com/search?q='+ content)
search.raise_for_status()

soup = bs4.BeautifulSoup(search.text, 'html.parser')
link  = soup.select('.r a')
linkopen = min(1, len(link))
webbrowser.open('https://google.com'+link.get[0]('href'))
'''