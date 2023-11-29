from typing import List

import datahub.emitter.mce_builder as builder
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.metadata.com.linkedin.pegasus2avro.datajob import DataJobInputOutputClass

# Construct the DataJobInputOutput aspect.
input_datasets: List[str] = [
    builder.make_dataset_urn(platform="mysql", name="hospitaldb.doctor", env="PROD"),
    builder.make_dataset_urn(platform="mysql", name="hospitaldb.patient", env="PROD"),
    builder.make_dataset_urn(platform="mysql", name="hospitaldb.appointment", env="PROD"),
    builder.make_dataset_urn(platform="mysql", name="hospitaldb.facility", env="PROD"),
]

output_datasets: List[str] = [
    builder.make_dataset_urn(platform="snowflake", name="landing.hospitaldb.doctor", env="PROD"),
    builder.make_dataset_urn(platform="snowflake", name="landing.hospitaldb.patient", env="PROD"),
    builder.make_dataset_urn(platform="snowflake", name="landing.hospitaldb.appointment", env="PROD"),
    builder.make_dataset_urn(platform="snowflake", name="landing.hospitaldb.facility", env="PROD")
]

input_data_jobs: List[str] = [
    builder.make_data_job_urn(
        orchestrator="airflow", flow_id="hospitaldb_ingestion_flow", job_id="hospitaldb_ingestion_job", cluster="PROD"
    )
]

datajob_input_output = DataJobInputOutputClass(
    inputDatasets=input_datasets,
    outputDatasets=output_datasets,
    inputDatajobs=input_data_jobs,
)

# Construct a MetadataChangeProposalWrapper object.
# NOTE: This will overwrite all of the existing lineage information associated with this job.
datajob_input_output_mcp = MetadataChangeProposalWrapper(
    entityUrn=builder.make_data_job_urn(
        orchestrator="airflow", flow_id="hospitaldb_ingestion_flow", job_id="hospitaldb_ingestion_job", cluster="PROD"
    ),
    aspect=datajob_input_output,
)

# Create an emitter to the GMS REST API.
emitter = DatahubRestEmitter("http://localhost:8080")

# Emit metadata!
emitter.emit_mcp(datajob_input_output_mcp)
