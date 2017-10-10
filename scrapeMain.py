# Collect from main URL
# Required info collected: (1a) Title & (1b) Description & (7) Social media pages and handles 

import soupTheLink
import sliceURL

def scrapeMain(pURL):
    souped = soupTheLink.soupTheLink(pURL)
    
    # Collect site title
    try:
        siteTitle = souped.title.get_text()
        siteTitle = str(siteTitle)
        if len(siteTitle) == 0:
            siteTitle = sliceURL.sliceURL(pURL).replace('.com', '').replace('/', '')
        print('title: ', siteTitle)
    except AttributeError:
        siteTitle = 'No title found.'
        
    # Collect site description
    try:
        siteDescription = souped.find(id='site-description').get_text()
        
        if len(siteDescription) == 0:
            siteDescription = souped.find(name='description').get_text()
            
            
        print('description: ', siteDescription)
    except AttributeError:
        siteDescription = 'No description found.'
    
    # Collect social media
    commonSocialMedia = ['facebook', 'instagram', 'youtube', 'twitter', 'pinterest', 'linkedin', 'google', 'yelp', 'tumblr', 'github']

    listedURLs = [link.get('href') for link in souped.find_all('a')]
    socialsOnSite=[]

    for link in listedURLs:

        for social in commonSocialMedia:
            try:
                if social in link:
                    socialsOnSite.append(link)
                else:
                    continue
            except TypeError:
                continue

    print('social media: ', socialsOnSite)
    
    if len(socialsOnSite) == 0:
        socialsOnSite.append('No socials found.')
    
    return siteTitle, siteDescription, socialsOnSite