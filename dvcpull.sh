#!/bin/bash

dvc config core.autostage true
dvc pull
python3 main.py
dvc add data-s3/
dvc add models-s3/
dvc add scripts-s3/
dvc push
