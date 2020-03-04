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

        