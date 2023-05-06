import os
from dotenv import load_dotenv
    

load_dotenv('.env')


BASE_PATH = os.getenv('BASE_PATH')
HELLO_WORLD = os.getenv('HELLO_WORLD')