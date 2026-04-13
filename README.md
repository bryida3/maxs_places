INSTALLATION INSTRUCTIONS:

Python3 must be installed, along with pip.

INSTALL PYTHON DEPENDENCIES:
  pip3 install -r requirements.txt

INSTALL ELASTICSEARCH:
  wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.17.13-darwin-x86_64.tar.gz
  tar -xzf elasticsearch-7.17.13-darwin-x86_64.tar.gz

RUN ELASTICSEARCH:
  elasticsearch-7.17.13/bin/elasticsearch

RUN DJANGO:
  python3 manage.py runserver

Navigate to localhost:8000/sites/ in your web browser!
