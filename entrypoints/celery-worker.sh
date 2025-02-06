#!/bin/bash

cd src

celery -A application.tasks worker -l INFO -Q $CELERY_QUEUE
