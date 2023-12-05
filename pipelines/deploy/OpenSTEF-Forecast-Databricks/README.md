# OpenSTEF Forecast with RTDIP
This article provides a guideline for making creating a prediction with historic data using OpenSTEF's task and RTDIP components.

## Prerequisites
This pipeline job requires the packages:

* [RTDIP SDK](../../../../../getting-started/installation.md#installing-the-rtdip-sdk)

## Components
|Name|Description|
|---------------------------|----------------------|
|[DataBase](../../../../code-reference/integrations/openstef/database.md)|Database connection object to run OpenSTEF services.|
|[DefaultAuth](../../../../code-reference/authentication/azure.md)|Default credential for Azure Active Directory authentication.|

## Configuration
|Name|Description|
|---------------------------|----------------------|
|api_username|?|
|api_password|?|
|api_admin_username|?|
|api_admin_password|?|
|api_url|?|
|pcdm_host|Databricks server hostname. This is the URL for your Databricks workspace.|
|pcdm_token|Token to connect to your workspace. Please see [here](../../../../code-reference/authentication/azure.md) for different ways to authenticate using RTDIP.|
|pcdm_port|Port used by your server.|
|pcdm_http_path|Databricks compute resources URL, found under the connection details for your SQL warehouse.|
|pcdm_catalog|Catalog name containing your tables.|
|pcdm_schema|Schema name containing your tables.|
|db_host|Databricks server hostname. This is the URL for your Databricks workspace.|
|db_token|Token to connect to your workspace. Please see [here](../../../../code-reference/authentication/azure.md) for different ways to authenticate using RTDIP.|
|db_port|Port used by your server.|
|db_http_path|Databricks compute resources URL, found under the connection details for your SQL warehouse.|
|db_catalog|Catalog name containing your tables.|
|db_schema|Schema name containing your tables.|
|proxies|Proxies|
|externally_posted_forecasts_pids|List of externally posted forecast pids.|
|teams_alert_url|Teams alert url.|
|teams_monitoring_url|Teams monitoring url.|
|known_zero_flatliners|List of pids with known zero flatflines.|
|paths_mlflow_tracking_uri|Path to MLflow tracking URI.|
|paths_artifact_folder|Path to artifact folder.|

## Example

```python
--8<-- "https://raw.githubusercontent.com/rodalynbarce/samples/feature/integration/pipelines/deploy/OpenSTEF-Forecast-Databricks/pipeline.py"
```
