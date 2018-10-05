def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_url = page.find('"', start_link)
    end_url = page.find('"', start_url+1)
    url = page[start_url+1:end_url]
    next_target = page[end_url+1:]
    return url,end_url

def all_links(page):
    while True:
        url, end_url = get_next_target(page)
        if url:
            print url
            page = page[end_url+1:]
        else:
            break