#!/bin/bash

cd src

celery -A application.tasks worker -l INFO -B
#celery -A application.tasks beat -l INFO
