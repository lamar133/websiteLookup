# Required info collected: (8) Does it have an e-commerce platform somewhere on the site

import soupTheLink

def getEcommerce(pSlicedURL):
    builtWithURL = "https://api.builtwith.com/v12/api.xml?KEY=dbf200b7-11db-4699-b85b-fac4ed4bae8a&HIDEDL=yes&LOOKUP=" + slicedURL
    soupedBuiltWithURL = soupTheLink.soupTheLink(builtWithURL)
    eCommercePlatforms=[]
    for platforms in soupedBuiltWithURL.find_all('category'):
        if platforms.get_text() == 'eCommerce':
            platform = platforms.next_element.next_element
            platform = str(platform)

            if platform[:6] == "<name>":
                eCommercePlatforms.append(platform.replace("<name>",'').replace("</name>",''))

    print("eCommercePlatforms: ", eCommercePlatforms)
    return eCommercePlatforms