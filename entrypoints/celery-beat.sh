#!/bin/bash

cd src

celery -A application.tasks beat -l INFO
