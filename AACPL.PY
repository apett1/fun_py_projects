from selenium import webdriver 
from bs4 import BeautifulSoup

author_list = ['Nicole Perlroth','Mark Solms','Patrick Harpur','Bob Boilen','Jaron Lanier','Hallam Stevens','Wumen Huikai','Adyashanti','Stephen Wolfram','Henry Shukman','W. Brian Arthur','Yuanwu Keqin','Hans Moravec','Nick Bostrom','Stephanie Kelton','Geoffrey B. West','Brian Greene','Max  Tegmark','Chiara Marletto','Julian Barbour','Gad Saad','Ed Finn','Sara Imari Walker','Marcus Aurelius','Sam Harris','Daniel C. Dennett','David Whyte','Massimo Pigliucci','Lawrence C. Becker','James Nestor','J. Doyne Farmer','Christopher G. Langton','Richard G. Wilkinson','Jim Paul','C.G. Jung','Shankar Vedantam','Robert Lanza','Jeremy England','Gaia Vince','David Quammen','Ben Ehrenreich','Steven  Dudley','Zach St. George','Nassim Nicholas Taleb','David Spiegelhalter','Bruce Hoffman','Carl T. Bergstrom','Melanie  Mitchell','John von Neumann','Toby  Ord','Leslie Kean','Andriy Burkov','Pedro Domingos','Neil Wilkins','David C. Krakauer','John H.  Miller','T. Colin Campbell','Vaclav Smil','Diane Tavenner','Stephen Harrigan','Suketu Mehta','Christian List','James C. Collins']

browser = webdriver.Chrome('chromedriver')

def has_hits_xpath(xpath):
  try:
    browser.find_element_by_xpath(xpath)
    return True
  except:
    return False

for authors in author_list:
  browser.get("https://catalog.aacpl.net/Search/Results?lookfor=" + authors + "&basicType=Author&basicType=Author&filter[]=format_category_aacpl%3A%22Audio+Books%22&filter[]=availability_toggle_aacpl%3A%22Available+Online%22&sort=relevance&view=list&searchSource=local")
  if has_hits_xpath('//*[@id="searchInfo"]/div[3]/div[1]'):
    print(f"{authors}: hits exist")
  else:
    print("0")
  

#excel formula is ="'" & A1 & "',"