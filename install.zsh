#!/bin/zsh

echo "Creating venv..."
python3 -m venv .maxs_places
source .maxs_places/bin/activate

echo "Installing Python Dependencies..."
pip3 install -r requirements.txt

echo "Installing ElasticSearch..."
curl -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.17.13-darwin-x86_64.tar.gz
tar -xzf elasticsearch-7.17.13-darwin-x86_64.tar.gz && rm elasticsearch-7.17.13-darwin-x86_64.tar.gz

echo "Building Search Indexes..."
./manage.py rebuild_index --noinput

echo "Done!"
deactivate
