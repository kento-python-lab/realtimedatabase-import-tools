# coding: UTF-8

import os
from os.path import join, dirname
from dotenv import load_dotenv
import json
import glob
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import ulid




print(sorted(glob.glob('./output/*')))
