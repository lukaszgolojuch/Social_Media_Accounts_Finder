import mechanize
from bs4 import BeautifulSoup as soup

#Function which use mechanize and soup to browse our google request and unable us scrapping on it
def find_soup(name, surname, city, platform):

    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    #Our request
    url="https://www.google.com/search?q="+name+"+"+surname+"+"+platform+"+"+city
    webpage = br.open(url)

    return soup(webpage, "html.parser")

#Function that searches for an account link on Facebook
def facebook_link(name, surname, city):

    soup = find_soup(name, surname, city, "facebook")

    facebook_count=0

    for a in soup.find_all('a', href=True):

        if a['href'].rfind("facebook.com") != -1 and facebook_count==0:
            facebook_link_before=a['href']
            # We cut needed fragment of link to facebook account
            facebook_link=facebook_link_before[7:facebook_link_before.find("&")]
            facebook_count=1
            return facebook_link

    return 0

#Function that searches for an account link on Instagram
def instagram_link(name, surname, city):

    soup = find_soup(name, surname, city, "instagram")

    instagram_count=0

    for a in soup.find_all('a', href=True):

        if a['href'].rfind("instagram.com") != -1 and instagram_count==0:
            instagram_link_before=a['href']
            # We cut needed fragment of link to instagram account
            if instagram_link_before.rfind("%") != -1:
                instagram_link=instagram_link_before[7:instagram_link_before.find("%")]
                instagram_count=1
                return instagram_link
            else:
                instagram_link=instagram_link_before[7:instagram_link_before.find("&")]
                instagram_count=1
                return instagram_link
    
    return 0

#Function that searches for an account link on LinkedIn
def linkedin_link(name,surname,city):

    soup = find_soup(name, surname, city, "LinkedIn")

    linkedin_count=0

    for a in soup.find_all('a', href=True):
        if a['href'].find("linkedin.com") != -1 and linkedin_count==0:
            linkedin_link_before=a['href']
            linkedin_count=1
            # We cut needed fragment of link to linkedin account
            linkedin_link=linkedin_link_before[7:linkedin_link_before.find("&")]

    return linkedin_link
    
    return 0


