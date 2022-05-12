from django.shortcuts import redirect, render
from random import choice
from . import util
from markdown2 import Markdown

markdown = Markdown()
def index(request):
    print(util.list_entries())
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    body = util.get_entry(entry)
    return render(request, "encyclopedia/entry.html",{
    "entry": entry,
    "entry_body": markdown.convert(body)
    })

def new(request):
    
    return render(request, "encyclopedia/new.html")

def random(request):
    entries = util.list_entries()
    print(entries)
    rnd = choice(entries)
    return redirect("entry", rnd)

def new_entry(request):
    form = request.POST
    new_title = form["new_title"]
    new_text = form["new_text"]
    if new_title == "":
        return False
    util.save_entry(new_title, new_text)
    return redirect("entry", new_title)

def search_results(request):
    query = request.GET["q"]
    if util.get_entry(query):
        return redirect("entry", query)
    else:
        print(util.list_entries)
        query_list = [i for i in util.list_entries() if query.lower() in i.lower()]
        return render(request, "encyclopedia/search_results.html", {
            "search_results" : query_list
    })

def edit(request):
    body = util.get_entry(request.POST["title"])
    title = request.POST["title"]
    return render(request, "encyclopedia/edit.html",{
    "entry": title,
    "entry_body": body
    })