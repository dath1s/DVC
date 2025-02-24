import os
import shutil

listdir = os.listdir()

if not os.path.exists('data-s3'):
    os.makedirs('data-s3')
if not os.path.exists('models-s3'):
    os.makedirs('models-s3')
if not os.path.exists('scripts-s3'):
    os.makedirs('scripts-s3')

shutil.copytree('data-docker', 'data-s3', dirs_exist_ok=True)
shutil.copytree('scripts-docker', 'scripts-s3', dirs_exist_ok=True)
shutil.copytree('models-docker', 'models-s3', dirs_exist_ok=True)
