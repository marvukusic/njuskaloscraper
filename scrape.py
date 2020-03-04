from services.scrape_service import scrapeContent
from services.file_service import FileService
from services.email_service import sendMail
from services.argument_parser import ArgumentParser
from helper.url_builder import buildUrl

import numpy as np
import os

appPath = os.path.dirname(os.path.abspath(__file__))
fileService = FileService(appPath)

arguments = ArgumentParser()
url = buildUrl(arguments)

currentBikeList = scrapeContent(url)
storedBikeList = fileService.readFromFile(arguments.fileName)

newBikesExists = not np.array_equal(currentBikeList, storedBikeList)
if newBikesExists:
    newBikes = [item for item in currentBikeList if item not in storedBikeList]

    if len(newBikes):
        sendMail(arguments.email, newBikes)

    fileService.writeToFile(arguments.fileName, currentBikeList)


