# Taking a list of names from a website, snag the locations of the artist
# based on their Wikipedia information


# Bring in the required libraries
import urllib2
from bs4 import BeautifulSoup


# Create a quick and dirty place holder for what gets processed
foundListings = []


#   CSS made it a pain to collect directly from the website;
#   Make due with a flat file collected from contractor

with open("listedas.txt","r") as rankerfile:
    counter = 1
    for each in rankerfile.readlines():
        if " is listed (or ranked) " in each:
            bandName = each[0:each.index(" is listed ")]
            webrank = int(each[each.index(") ")+2:each.index(" on the list")])

            #   There are going to be pages that don't line up; get over it and get the bulk
            #   with the standard Wikipedia URL
            wikiInsert = "https://en.wikipedia.org/wiki/" + bandName.replace(" ","_").replace("'","")
            foundListings.append([bandName,webrank,wikiInsert])


# Quick and dirty harcode to act as a shepard function
counter=list(range(1,501))
collectedRanks=[]


#   Start scrapping up based on research of three instances, a band, a musician and a producer
for each in foundListings:
    collectedRanks.append(each[1])

    #print each
    locationLn = -1

    #   Some webpages may not return so clean; give it a go. If it doesn't work, move uon
    #   uninterrupted
    try:
        accessWiki = urllib2.urlopen(each[2])

        #   the idx is where the line was found; the next line is where the information is found
        for idx,eachWiki in enumerate(accessWiki):
            if '<th scope="row">Born</th>' in eachWiki:
                locationLn = int(idx+2)
                
            elif '<th scope="row">Origin</th>' in eachWiki:
                locationLn = int(idx+1)
                
            elif '<span class="birthplace">' in eachWiki:
                locationLn = int(idx+1)
                

        each.append(locationLn)
        #print each

    except:
        each.append(locationLn)
        #print each

# There's bound to be some missing, catch them and handle them later 
missingBands = list((set(counter)^set(collectedRanks)))

print "There are " + str(len(missingBands)) + " missing bands."
for each in missingBands:
    print "#" + str(each)


#   Parse out the location in a readable format by a gcoder.
for each in foundListings:
    if each[3] != -1:
        accessWiki = urllib2.urlopen(each[2])
        for idx,eachWiki in enumerate(accessWiki):
            if idx == each[3]:
                try:
                    soup = BeautifulSoup(eachWiki, 'html.parser')
                    print "\""+ each[0] + "\",\"" + soup.get_text().replace("\n","")+"\""
                except:
                    print "\""+ each[0] + "\",\"ERROR-REPROCESS\""
    else:
        print "\""+ each[0] + "\",\"ERROR-REPROCESS\""

#   Can defintely pipe to a file but why bother for a quick and easy out?


