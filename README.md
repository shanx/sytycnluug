sytycnluug
==========

So You Think You Can Netherlands Local Unix Users Group?

This is the app demoed at the 'Python: ter leering ende vermaeck' presentation on november 8th 2012 at the https://www.nluug.nl/ conference on software development by @janjaapdriessen and @shanx.

Installation instructions
-------------------------

To get this up & running on your own system, do the following:

 * Make sure you have python 2.7 installed on your computer with a working compiler chain
 * Install zc.buildout as a system dependency: `pip install zc.buildout` or `easy_install zc.buildout`
 * Clone the repo to your local computer: `git clone git://github.com/shanx/sytycnluug.git ~/sytycnluug`
 * Run buildout in the repository root: `cd ~/sytycnluug && buildout` (buildout takes some time to run to get all dependencies)
 * Install the database and run all the migrations: `./bin/django syncdb --migrate`
 * Import the talks using the scrape script: `./bin/python scrape.py |./bin/django import_talks`
 * Run the django development server: `./bin/django runserver`
 * In your browser go to: `127.0.0.1:8000/ratezzz/`

**NOTE**: You need a working internet connection, external javascript and css files are used from CDN's.

The steps in the presentation to build this application can be found in a seperate repo: https://github.com/shanx/nluug

