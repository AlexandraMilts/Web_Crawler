def get_next_target(page): #Find the 1st url on the page and define where it ends - to start looking for the new one
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_url = page.find('"', start_link)
    end_url = page.find('"', start_url+1)
    url = page[start_url+1:end_url]
    next_target = page[end_url+1:]
    return url,end_url

def get_all_links(page): #Get all the links on the page
    links = [] #Create the empty list of links
    while True: #Basically, forever, until break happens
        url, end_url = get_next_target(page) #Check if we have a url and where we start crawling
        if url: #If url exists
            list.append(url) #Add the url to the list
            page = page[end_url+1:] #Start crawling after the url
        else:
            break #Run until we run out of the urls on the page
    return list