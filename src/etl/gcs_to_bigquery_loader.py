schema = [
    bigquery.SchemaField("product_id", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("product_name", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("category", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("price", "FLOAT64", mode="NULLABLE"),
    bigquery.SchemaField("description", "STRING", mode="NULLABLE"),
]

job_config = bigquery.LoadJobConfig(
    schema=schema, # The correct schema is now provided
    create_disposition="CREATE_IF_NEEDED",
    write_disposition="WRITE_EMPTY",
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
)

load_job = client.load_table_from_uri(
    source_uris,
    table_id,
    job_config=job_config,
)