# OpenSTEF Basecase Forecast with RTDIP
This article provides a guideline for creating a basecase forecast with OpenSTEF's task and RTDIP components.

## Prerequisites
This pipeline job requires the packages:

* [rtdip-sdk](../../../../../getting-started/installation.md)

## Components
|Name|Description|
|---------------------------|----------------------|
|[DataBase](../../../../code-reference/integrations/openstef/database.md)|Database connection object to run OpenSTEF services.|


## Example

```python
--8<-- "https://raw.githubusercontent.com/rodalynbarce/samples/feature/integration/pipelines/deploy/OpenSTEF-Basecase-Forecast-Databricks/pipeline.py"
```
