#!/bin/zsh

source .maxs_places/bin/activate
(trap 'kill 0' SIGINT; (python3 manage.py runserver) & (elasticsearch-7.17.13/bin/elasticsearch))
deactivate
