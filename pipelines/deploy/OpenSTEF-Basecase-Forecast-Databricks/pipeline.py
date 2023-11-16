from typing import Union
from pydantic.v1 import BaseSettings
from openstef.tasks import create_basecase_forecast as task
from src.sdk.python.rtdip_sdk.authentication.azure import DefaultAuth
from src.sdk.python.rtdip_sdk.integrations.openstef.database import DataBase

auth = DefaultAuth().authenticate()
token = auth.get_token("2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default").token


class ConfigSettings(BaseSettings):
    api_username: str = "None"
    api_password: str = "None"
    api_admin_username: str = "None"
    api_admin_password: str = "None"
    api_url: str = "None"
    pcdm_host: str = "{DATABRICKS-SERVER-HOSTNAME}"
    pcdm_token: str = token
    pcdm_port: int = 443
    pcdm_http_path: str = "{SQL-WAREHOUSE-HTTP-PATH}"
    pcdm_catalog: str = "{YOUR-CATALOG-NAME}"
    pcdm_schema: str = "{YOUR-SCHEMA-NAME}"
    db_host: str = "{DATABRICKS-SERVER-HOSTNAME}"
    db_token: str = token
    db_port: int = 443
    db_http_path: str = "{SQL-WAREHOUSE-HTTP-PATH}"
    db_catalog: str = "{YOUR-CATALOG-NAME}"
    db_schema: str = "{YOUR-SCHEMA-NAME}"
    proxies: Union[dict[str, str], None] = None
    externally_posted_forecasts_pids: list = None


config = ConfigSettings()

def main():
    database = DataBase(config)
    task.main(config=config, database=database)


if __name__ == "__main__":
    main()