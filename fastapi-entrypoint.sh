#!/bin/bash

cd src

uvicorn main:app --host $WEB_HOST --port $WEB_PORT
