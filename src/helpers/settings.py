from pydantic_settings import BaseSettings

'''
Settings class inherit BaseSettings, and define the settings (datatypes)

Config is nested class provide the metadata to fill the settings with.
'''


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    
    class Config:
        env_file = ".env" #predefined with pydantic

def get_settings():
    return Settings()