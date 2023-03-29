import os
from dotenv import load_dotenv


if "APP_ENV" in os.environ and os.environ['APP_ENV'] == 'production':
    hello_world = os.environ['HELLO_WORLD']
    health_check_endpoint = os.environ['HEALTH_CHECK_ENDPOINT']
    base_path = os.environ['BASE_PATH']

else:
    load_dotenv('.env')
    hello_world = os.getenv('HELLO_WORLD')
    health_check_endpoint = os.getenv('HEALTH_CHECK_ENDPOINT')
    base_path = os.getenv('BASE_PATH')

    