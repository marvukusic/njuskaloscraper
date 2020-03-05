def buildUrl(args):
    website =           "https://www.njuskalo.hr/"
    section =           "%s" % args.section
    minPrice =          "?price%%5Bmin%%5D=%i" % args.minPrice
    maxPrice =          "&price%%5Bmax%%5D=%i" % args.maxPrice
    condition =         "&condition%5Bused%5D=1"
    location =          "&locationIds=%s" % args.location
    
    url = "".join([website, 
                    section, 
                    minPrice, 
                    maxPrice, 
                    condition,
                ])
    
    if args.location:
        url += location

    return url

def buildPaginatedUrls(url, maxPages):
    urls = []
    for idx in range(1, maxPages + 1):
        urls.append(url + "&page=%i" % idx)
    return urls