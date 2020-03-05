import argparse
import re
class ArgumentParser:
    def __init__(self):
        self.__configureArguments()
        self.__readArguments()
    
    def __configureArguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-e", "--email",      help="Set email",             required=True,      type=str)
        parser.add_argument("-m", "--min",        help="Set min price",         default=0,          type=int)
        parser.add_argument("-x", "--max",        help="Set max price",         default=100000000,  type=int)
        parser.add_argument("-s", "--section",    help="Set website section",   required=True,      type=str)
        parser.add_argument("-l", "--location",   help="Set location(s)",                           type=str)

        self.__args = parser.parse_args()
    
    def __readArguments(self):
        self.email = self.__args.email
        emailRegex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(emailRegex, self.email):
            print("Error: Email address invalid")
            exit(1)

        self.fileName = self.email.split("@")[0] + ".data"
        self.minPrice = self.__args.min
        self.maxPrice = self.__args.max
        self.section = self.__args.section

        locations = self.__args.location
        if locations:
            locationsArray = locations.split(',')
            codedLocations = [str(self.__locationCodes[location]) for location in locationsArray]
            self.location = "%7C".join(codedLocations)
        else:
            self.location = None
    
    __locationCodes = { "BB": "1150",
                        "BP": "1151",
                        "DN": "1152",
                        "ZG": "1153",
                        "IS": "1154",
                        "KA": "1155",
                        "KK": "1156",
                        "KZ": "1157",
                        "LS": "1158",
                        "ME": "1159",
                        "OB": "1160",
                        "PS": "1161",
                        "PG": "1162",
                        "SM": "1163",
                        "SD": "1164",
                        "SK": "1165",
                        "VA": "1166",
                        "VP": "1167",
                        "VS": "1168",
                        "ZD": "1169",
                        "ZA": "1170",
                        }

