import random
import string
import webbrowser



class UrlShorten:

  def __init__(self, link):
    self.link = link
    self.url_dict = {}
  
  def open_link(self):
    link = input('copy and paste the short link to access long link: ')
    try:
        origin_link = self.url_dict[link]
        webbrowser.open(origin_link)
    except:
      print('something goes wrong. MAY BE YOUR SYSTEM DO NOT WORK WITH WEBBROWSER MODULE')
      print('make sure you are copying collect text and make sure you have webbrowser in your system...')

  def generate_url_string(self):
    return 'https://url.com/' + ''.join(random.choices(string.ascii_letters + string.digits, k=6))

  def get_short_url(self):
    short_link = self.generate_url_string()
    self.url_dict[short_link] = self.link
    return self.url_dict
  

  

long_link = 'https://github.com/crepe-japheth/objectivity_challenge'

obj = UrlShorten(long_link)

short_link = obj.get_short_url()

print('the long link is : ' + ''.join(short_link.values()))
print('the short link is : ' + ''.join(short_link.keys()))


obj.open_link()


