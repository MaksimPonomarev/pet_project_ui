from pydantic import BaseModel, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class TestDataConfig(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter=".",
        extra="allow"
    )
    base_url: str
    test_data: TestDataConfig
    default_timeout: int = 40000
    navigation_timeout: int = 100000
    slow_mo: int


settings = Settings()


