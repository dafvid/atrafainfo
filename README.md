# atrafaweb
Serves a static web page generated from Minecraft map data. 

## Setup
1. Install Homebrew
2. `brew install python`
3. `git clone git@github.com:dafvid/atrafaweb.git`
4. `cd atrafaweb`
5. `python3 -m venv venv --system-site-packages`
6. `venv/bin/pip install -U pip`
7. `venv/bin/pip install -U wheel`
8. `venv/bin/pip install -r requirements.txt`

## How to: change the look and feel of the webpage
1. Update the web resources in /web 
2. Update the HTML-template in atrafadata/templates
3. Generate a new index.html in /web using `python3 test.py`
