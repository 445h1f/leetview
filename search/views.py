from django.shortcuts import render
from django.http import JsonResponse
from .db import DatabaseSearch

# database search class for searching problems and other advanced search
db = DatabaseSearch()

def search(request):
    context = {
        "title": "Search"
    }

    if request.method == 'POST':
        url = request.POST["url"]

        # basic url validation (if not matches with leetcode problem url path)
        if not url.startswith("https://leetcode.com/problems/"):
            # error 404 for invalid url
            context["error"] = "Invalid URL!"

            return render(request, 'search/404.html', context)

        # adding '/' if not in end of url
        if url[-1] != '/' :
            url += '/'

        result = db.getProblemData(url)

        if 'error' not in result:
            result["title"] = "Search Result"
            result["id"] = result["_id"]
            del result["_id"]

            context.update(result)

            return render(request, 'search/result.html', context)
        else:
            context["error"] = "Problem URL not found in Database🥲"

            return render(request, 'search/404.html', context)

    return render(request, 'search/search.html', context)
