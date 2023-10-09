from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#function to get any word and generate a response for it. from "encyclopedia" path.
def content_entry(request,word):
   return render(request, f"encyclopedia/{word}", {
        "entries": util.list_entries()
    }) 
    