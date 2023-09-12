import pymongo

class DatabaseSearch:
    """Class to manage search for leetcode questions """

    # mongodb client
    __mongo = pymongo.MongoClient('mongodb://localhost:27017')

    __leetcode = __mongo["leetcode"] # leetcode db
    __questions = __leetcode["questions"] # questions collection


    def getProblemData(self, url:str):
        """Returns question data for given url."""

        # querying for document containing url
        result = self.__questions.find_one({"url": url})

        if result is not None:
            # problem url found in db so returning it's data
            return result
        else:
            # not found
            return {"error": "problem url not found"}
