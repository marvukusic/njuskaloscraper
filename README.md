# DESCRIPTION
Scrapes Njuskalo website to let you know when new items are added

# USAGE 
Periodically run script using arguments from table below.

Argument  | Description                                                         | Default
--------- | ------------------------------------------------------------------- | ------------
--email   | Your email address                                                  | **required**
--section | Website section - part of url between `www.njuskalo.hr/` and `?`    | **required**
--min     | Minimal price filter                                                | 0
--max     | Maximal price filter                                                | 100000000

First run will send all items from njuskalo webasite matching the given filter criteria. 
Every subsequent run will send items that are newly added, if any.
    
# EXAMPLE
`python scrape.py --email my@email.com --section cestovni-bicikli --min 1000 --max 10000` 



