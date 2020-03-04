from services.scrape_service import scrapeContent, scrapeContentPaginated
from services.file_service import FileService
from services.email_service import sendMail
from services.argument_parser import ArgumentParser
from helper.url_builder import buildUrl, buildPaginatedUrls

import numpy as np
import os

itemsPerPage = 25

appPath = os.path.dirname(os.path.abspath(__file__))
fileService = FileService(appPath)

arguments = ArgumentParser()
url = buildUrl(arguments)

itemCount = scrapeContent(url)
maxPages = int(itemCount / itemsPerPage) + 1
urls = buildPaginatedUrls(url, maxPages)

currentItemList = scrapeContentPaginated(urls)
storedItemList = fileService.readFromFile(arguments.fileName)

newItemsExists = not np.array_equal(currentItemList, storedItemList)
if newItemsExists:
    newItems = [item for item in currentItemList if item not in storedItemList]

    if len(newItems):
        sendMail(arguments.email, newItems)

    fileService.writeToFile(arguments.fileName, currentItemList)


