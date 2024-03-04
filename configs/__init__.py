from pydantic_settings import BaseSettings, SettingsConfigDict


class Configs(BaseSettings):

    host: str
    port: int
    db_url: str

    model_config = SettingsConfigDict(
        env_file=(".env", ".env.prod")
    )
