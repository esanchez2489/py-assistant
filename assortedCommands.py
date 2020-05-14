import os
import weatherAPI as W
import webbrowser

class Commands:
    def __init__(self):
        self.confirm = ['yes', 'affirmative']
        self.cancel = ['no', 'negative', 'cancel']



    def respond(self, response):
        os.system('say ' + response)
        print (response)


    def discover(self, text):
        if 'what' in text and 'your name' in text:
            if 'my' in text:
                self.respond('You have not told me your name yet')
            else:
                self.respond ('My name is Pie Assistant')

        elif 'open website' in text:
            self.respond('I will open website')
            keyword = 'open website '
            splicer = (text.find(keyword))
            site = (text[splicer+len(keyword):])

            url = 'https:/www.'
            url = url + site
            print (url)
            try:
                webbrowser.open(url)
            except:
                self.respond('Unable to open the website')



        elif "search google for" in text:
            text = 'search google for foxes '
            keyword = 'search google for '

            splicer = (text.find(keyword))
            search_term = (text[splicer+len(keyword):])


            search = 'https://www.google.com/search?q=' + search_term
            webbrowser.open(search)



        elif "launch" in text or "open" in text:

            app = text.split(" ",1)[-1]
            # generally apps are in lowercase to open from terminal
            app= app.lower()
            self.respond("Opening " + app)
            try:
                if app in ['chrome', 'google']:
                    os.system('google-chrome &')
                else:    
                    os.system(app +' &' )
            except:
                self.respond('Application could not be opened')



        elif 'weather in' in text:
            keyword = 'weather in '
            splicer = (text.find(keyword))
            city = (text[splicer+len(keyword):])

            #returns a tuple, 1st = temp, 2nd = wind speed
            d = W.weather(city)
            temp = str(d[0])
            wind = str(d[1])

            self.respond('It is ' + temp +' degrees fahrenheit')
            self.respond('There is also a wind speed of ' + wind +'miles per hour')
        
        else:
            self.respond('I am unable to process that command')



