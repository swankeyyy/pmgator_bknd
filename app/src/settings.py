from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    # Debug mode
    DEBUG: bool = True
    
    # API prefix
    API_V1_STR: str
    API_PREFIX: str 
    
    # DB settings
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_ECHO: bool
    
    # DB URL
    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
    
settings = Settings()

