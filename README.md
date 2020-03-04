DESCRIPTION: 
    Scrapes Njuskalo website to let you know when new items are added

USAGE: 
    Periodically run script with following arguments:
    1. --email                      // Your email address 
    2. --section                    // Website section - can be found in url between "www.njuskalo.hr/" and "?"
    3. --min                        // Minimal price filter (default=0)
    4. --max                        // Maximal price filter (default=100000000)

    First run will send all items from njuskalo webasite matching the given filter criteria. Every subsequent run will send items that are newly added, if any.
    
EXAMPLE:
    python scrape.py --email my@email.com --section cestovni-bicikli --min 1000 --max 10000 



