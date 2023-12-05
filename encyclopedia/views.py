from django.shortcuts import render
from . import util
from markdown2 import markdown
from django import forms

class inputForm(forms.Form):
    entry_title = forms.CharField(label= "Title")
    content = forms.CharField(widget=forms.Textarea, label= "Content")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
        
    return render(request, "encyclopedia/entry.html", {
        "title": markdown(util.get_entry(title))

    })


def search(request):

    query = request.GET['query']
    entries = util.list_entries()
    result = util.get_entry(query)

    if result is not None:
        return render(request, "encyclopedia/entry.html", {
            "title": markdown(result)
        })

    else:
        list = []
        for entry in entries:
            if query.upper() in entry.upper():
                list.append(entry)
        return render(request, 'encyclopedia/index.html', {'entries': list, 'head': query, 'search': True})


def new_page(request):
    # list = util.list_entries() 
    # entry = util.get_entry(title)
    # form = inputForm()
    # form = inputForm(request.POST)  
    if request.method == "POST":
                     
        if inputForm(request.POST).is_valid:
            heading = inputForm(request.POST).cleaned_data["entry_title"]
            content = inputForm(request.POST).cleaned_data['content']
            list += [heading]
            # entry += content
            new_entry = util.save_entry(heading, content)
            return render(request, 'encyclopedia/entry.html', {'title': new_entry})
        else:        
            return render(request, 'encyclopedia/new_page.html', {'form': inputForm(request.POST)})
    return render(request, 'encyclopedia/new_page.html', {"form": inputForm()})

# def search(request):
#     keyword = request.GET['query']
#     result = util.get_entry(keyword)
#     entries = util.list_entries()
#     new_entries = []


#     context = {
#         "title": result,
#         "head": keyword
#     }

#     for entry in entries:

#         if result: # if kywword matches all the characters
#             return render(request, "encyclopedia/search.html", context)
#         elif keyword.lower() in entry.lower(): # if kywword matches any of the characters
#             new_entries.append(entry)
#         elif not result and keyword.lower() not in entry:
#             return render(request, "encyclopedia/notfound.html")
#     return render(request, "encyclopedia/new_list.html",{"entries": new_entries, "head": keyword})

    # return render(request, "encyclopedia/new_list.html",{"entries": new_list, "head": keyword})


# def search(request):
#     keyword = request.GET['query']
#     entries = util.list_entries()
#     new_list = []

#     if keyword == entries:
#         return render(request, "encyclopedia/entry.html", {
#             "title": util.get_entry(keyword)

#         })

#     elif keyword in entries:
#         for entry in entries:
#             new_list.append(entry)
#             return render(request, "encyclopedia/search.html", {
#                 "title": new_list,
#                 "head": keyword
#             })
#     else:
#         return render(request, "encyclopedia/notfound.html")


# def search(request):
#     keyword = request.GET['query']
#     entries = util.list_entries()
#     new_list = []

#     for entry in entries:
#         if keyword in entry:
#             new_list.append(entry)
#             return render(request, "encyclopedia/search.html", {
#                 "entry": new_list,
#                 "head": keyword

#             })
#         else:
#            return render(request, "encyclopedia/notfound.html")


# cores = [70, 60, 80, 90, 50]
# filtered = filter(lambda score: score >= 70, scores)

# print(list(filtered))
