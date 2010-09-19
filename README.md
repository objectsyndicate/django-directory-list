Introduction, History, and Installation
---------------------------------------

We built this application for a client who had more than 100 PDFs they wanted
their clients to see. Based on the directory structure this was the best fit,
we built the app, installed it, and then just threw the files in the directory
and included the template. All of the files can be viewed at a URL built from
the for loop.

## Installation
1. Download the application
2. Run
	python setup.py install
3. Add the directory\_list application to your INSTALLED\_APPS
4. Edit the _views.py_ and set the path you want displayed
5. Move the template into place and configure the URLs
