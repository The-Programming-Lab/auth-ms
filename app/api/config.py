import os
from dotenv import load_dotenv


if "APP_ENV" in os.environ and os.environ['APP_ENV'] == 'production':
    try:
        hello_world = os.environ['HELLO_WORLD']
    except:
        hello_world = 'An error occurred while trying to get the environment variable HELLO_WORLD'
    try:
        health_check_endpoint = os.environ['HEALTH_CHECK_ENDPOINT']
    except:
        health_check_endpoint = '/health-check'
    try:
        base_path = os.environ['BASE_PATH']
    except:
        base_path = '/error'
    

else:
    load_dotenv('.env')
    hello_world = os.getenv('HELLO_WORLD')
    health_check_endpoint = os.getenv('HEALTH_CHECK_ENDPOINT')
    base_path = os.getenv('BASE_PATH')

    