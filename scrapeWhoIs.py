# Collect WhoIs source info
# Required info collected: (2) Street Address with Country & (3) Phone Number & (4) Admin Contact  

import soupTheLink
import sliceURL

def scrapeWhoIs(pURL):
    slicedURL = sliceURL.sliceURL(pURL) 
    
    whoIsURL = "https://who.is/whois/" + slicedURL
    
    soupedWhoIsURL = soupTheLink.soupTheLink(whoIsURL)

    nameNum = 0
    organizationNum = 0
    addressNum = 0
    cityNum = 0
    stateOrProvinceNum = 0
    postalCodeNum = 0
    countryNum = 0
    phoneNum = 0
    emailNum = 0

    registrantName = ""
    registrantOrganization = ""
    registrantAddress = ""
    registrantCity = ""
    registrantStateOrProvince = ""
    registrantPostalCode = ""
    registrantCountry = ""
    registrantPhone = ""
    registrantEmail = ""
    
    adminName = ""
    adminOrganization = ""
    adminAddress = ""
    adminCity = ""
    adminStateOrProvince = ""
    adminPostalCode = ""
    adminCountry = ""
    adminPhone = ""
    adminEmail = ""
    
    technicalName = ""
    technicalOrganization = ""
    technicalAddress = ""
    technicalCity = ""
    technicalStateOrProvince = ""
    technicalPostalCode = ""
    technicalCountry = ""
    technicalPhone = ""
    technicalEmail = ""
    
    for header in soupedWhoIsURL.find_all('strong'):
        
        if header.get_text() == "Name":
            nameNum += 1
            name = header.parent.next_sibling
            name = name.get_text()
            
            if nameNum == 1:
                registrantName = name
            elif nameNum == 2:
                adminName = name
            elif nameNum == 3:
                technicalName = name
        elif header.get_text() == "Organization":
            organizationNum += 1
            organization = header.parent.next_sibling
            organization = organization.get_text()
            
            if organizationNum == 1:
                registrantOrganization = organization
            elif organizationNum == 2:
                adminOrganization = organization
            elif organizationNum == 3:
                technicalOrganization = organization
        elif header.get_text() == "Address":
            addressNum += 1
            address = header.parent.next_sibling
            address = address.get_text()
            
            if addressNum == 1:
                registrantAddress = address
            elif addressNum == 2:
                adminAddress = address
            elif addressNum == 3:
                technicalAddress = address
        elif header.get_text() == "City":
            cityNum += 1
            city = header.parent.next_sibling
            city = city.get_text()
            
            if cityNum == 1:
                registrantCity = city
            elif cityNum == 2:
                adminCity = city
            elif cityNum == 3:
                technicalCity = city
        elif header.get_text() == "State / Province":
            stateOrProvinceNum += 1
            stateOrProvince = header.parent.next_sibling
            stateOrProvince = stateOrProvince.get_text()
            
            if stateOrProvinceNum == 1:
                registrantStateOrProvince = stateOrProvince
            elif stateOrProvinceNum == 2:
                adminStateOrProvince = stateOrProvince
            elif stateOrProvinceNum == 3:
                technicalStateOrProvince = stateOrProvince
        elif header.get_text() == "Postal Code":
            postalCodeNum += 1
            postalCode = header.parent.next_sibling
            postalCode = postalCode.get_text()
            
            if postalCodeNum == 1:
                registrantPostalCode = postalCode
            elif postalCodeNum == 2:
                adminPostalCode = postalCode
            elif postalCodeNum == 3:
                technicalPostalCode = postalCode
        elif header.get_text() == "Country":
            countryNum += 1
            country = header.parent.next_sibling
            country = country.get_text()
            
            if countryNum == 1:
                registrantCountry = country
            elif countryNum == 2:
                adminCountry = country
            elif countryNum == 3:
                technicalCountry = country
        elif header.get_text() == "Phone":
            phoneNum += 1
            phone = header.parent.next_sibling
            phone = phone.get_text()
            
            if phoneNum == 1:
                registrantPhone = phone
            elif phoneNum == 2:
                adminPhone = phone
            elif phoneNum == 3:
                technicalPhone = phone
        elif header.get_text() == "Email":
            emailNum += 1
            email = header.parent.next_sibling
            email = "https://who.is/" + email.img['src']
            
            if emailNum == 1:
                registrantEmail = email
            elif emailNum == 2:
                adminEmail = email
            elif emailNum == 3:
                technicalEmail = email
                
    print("adminAddress", adminAddress)
    print("adminCity", adminCity)
    print("adminStateOrProvince", adminStateOrProvince)
    print("adminCountry", adminCountry)
    print("adminPhone", adminPhone)
    print("adminEmail", adminEmail)
    
    if len(adminAddress) == 0:
        adminAddress = 'No address found.'
    if len(adminCity) == 0:
        adminCity = 'No city found.'
    if len(adminStateOrProvince) == 0:
        adminStateOrProvince = 'No state or province found.'
    if len(adminCountry) == 0:
        adminCountry = 'No country found.'
    if len(adminPhone) == 0:
        adminPhone = 'No phone found.'
    if len(adminEmail) == 0:
        adminEmail = 'No email found.'
    
    return adminAddress, adminCity, adminStateOrProvince, adminCountry, adminPhone, adminEmail