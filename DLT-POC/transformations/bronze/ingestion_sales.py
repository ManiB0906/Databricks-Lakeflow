import dlt

# Expectations
# https://docs.databricks.com/aws/en/dlt/expectations
sales_expectations = {
    "rule1": "sales_id is not NULL"
}

# Create Empty Bronze Streaming Table (create_target_table() and create_streaming_live_table() functions are deprecated)
# https://docs.databricks.com/aws/en/dlt-ref/dlt-python-ref-streaming-table
dlt.create_streaming_table(
    name="sales_stg",
    expect_all_or_drop=sales_expectations
)

# Create Flows to Append East and West Sales Data
# https://docs.databricks.com/aws/en/dlt-ref/dlt-python-ref-append-flow
@dlt.append_flow(target="sales_stg")
def east_sales():
    df = spark.readStream.table("manib0906.source.sales_east")
    return df

@dlt.append_flow(target="sales_stg")
def west_sales():
    df = spark.readStream.table("manib0906.source.sales_west")
    return df