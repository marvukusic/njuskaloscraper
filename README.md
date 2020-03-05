# DESCRIPTION
Scrapes Njuskalo website to let you know when new items are added

# USAGE 
Periodically run script using arguments from table below.

Argument   | Description                                                          | Default
---------- | -------------------------------------------------------------------- | ------------
--email    | Your email address                                                   | **required**
--section  | Website section - part of url between `www.njuskalo.hr/` and `?`     | **required**
--location | Region filter - comma separated abbreviated regions, see table below | All regions
--min      | Minimal price filter                                                 | 0
--max      | Maximal price filter                                                 | 100000000

First run will send all items from njuskalo webasite matching the given filter criteria. 
Every subsequent run will send items that are newly added, if any.

## Regions
Abbreviation    | Region
BB              | Bjelovarsko-bilogorska županija
BP              | Brodsko-posavska županija
DN              | Dubrovačko-neretvanska županija
IS              | Istarska županija 
KA              | Karlovačka županija
KK              | Koprivničko-križevačka županija 
KZ              | Krapinsko-zagorska županija 
LS              | Ličko-senjska županija 
ME              | Međimurska županija 
OB              | Osječko-baranjska županija 
PS              | Požeško-slavonska županija 
PG              | Primorsko-goranska županija 
SM              | Sisačko-moslavačka županija 
SD              | Splitsko-dalmatinska županija
VA              | Varaždinska županija 
VP              | Virovitičko-podravska županija 
VS              | Vukovarsko-srijemska županija 
ZD              | Zadarska županija 
ZA              | Zagrebačka županija 
SK              | Šibensko-kninska županija 
ZG              | Grad Zagreb 
    
# EXAMPLE
`python scrape.py --email my@email.com --section cestovni-bicikli --location SD,ZD --min 1000 --max 10000` 



