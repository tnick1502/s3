from pydantic import BaseSettings, Field
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.normpath("env.txt"))

class Configs(BaseSettings):
    endpoint_url: str = Field(..., env='AWS_URI')
    aws_access_key_id: str = Field(..., env='AWS_ACCCESS_KEY')
    service_name: str = Field(..., env='AWS_SERVICE_NAME')
    aws_secret_access_key: str = Field(..., env='AWS_SECRET_KEY')
    region_name: str = Field(..., env='AWS_REGION')
    bucket: str = Field(..., env='AWS_BUCKET')

configs = Configs()