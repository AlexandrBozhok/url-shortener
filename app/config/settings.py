from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env',
        env_file_encoding='utf-8',
    )

    secret_key: str

    db_name: str
    db_host: str
    db_port: int | None = 5432
    db_user: str
    db_password: str

    @property
    def db_url(self):
        return f"postgresql://{self.db_user}:{self.db_password}" \
               f"@{self.db_host}:{self.db_port}/{self.db_name}"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


app_settings = get_settings()
