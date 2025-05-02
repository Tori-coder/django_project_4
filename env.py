import os
from dotenv import load_dotenv
load_dotenv()

os.environ.setdefault(
    "DATABASE_URL", os.getenv("DATABASE_URL"))

os.environ['SECRET_KEY'] = os.getenv('SECRET_KEY')

os.environ['GOOGLE_CLIENT_ID']= os.getenv('GOOGLE_CLIENT_ID')
os.environ['GOOGLE_CLIENT_SECRET']= os.getenv('GOOGLE_CLIENT_SECRET')