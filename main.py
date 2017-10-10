# Main function

import sliceURL
import scrapeMain
import scrapeWhoIs
import scrapeAlexa
import getTimezone
import getEcommerce

def runSearch(pURL):
    
    slicedURL = sliceURL.sliceURL(pURL)
    siteTitle, siteDescription, socialsOnSite = scrapeMain.scrapeMain(pURL)
    adminAddress, adminCity, adminStateOrProvince, adminCountry, adminPhone, adminEmail = scrapeWhoIs.scrapeWhoIs(pURL)
    score, keywords = scrapeAlexa.scrapeAlexa(slicedURL)
    
    timezoneId=''
    timezoneName=''
    if adminCity == 'No city found.' or adminStateOrProvince == 'No state or province found.':
        timezoneId = 'No timezone ID found.'
        timezoneName = 'No timezone name found.'
    else:
        timezoneId, timezoneName = getTimezone.getTimezone(adminCity, adminStateOrProvince)
    
    #eCommercePlatforms = getEcommerce.getEcommerce(slicedURL)
    
    requiredInfo = {'Title': siteTitle, 'Description': siteDescription, 'Socials': socialsOnSite, 'Address': adminAddress, 'City': adminCity, 'State': adminStateOrProvince, 'Country': adminCountry, 'Phone': adminPhone, 'Email': adminEmail, 'Alexa Score': score, 'Keywords': keywords, 'Timezone ID': timezoneId, 'Timezone Name': timezoneName}
    
    return requiredInfo