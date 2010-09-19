# Create your views here.

import os
from django.http import HttpResponse
from django.shortcuts import render_to_response

def filetree(request):
    path="/path/to/dir/" 
	# insert the path to the directory including the trailing '/'
    dirList=sorted(os.listdir(path))
    return render_to_response('directory_list/list.html', {'dirlist': dirList})