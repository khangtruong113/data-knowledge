import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'nghia')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'nghia')
DATABASE_HOST = os.getenv('DATABASE_HOST', '0.0.0.0')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'myapp')
