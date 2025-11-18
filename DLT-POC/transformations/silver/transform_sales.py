import dlt
from pyspark.sql.functions import col, expr

# Create View to Encrich Data
@dlt.view(
    name="sales_enr_view"
)
def sales_enr_view():
    df = spark.readStream.table("sales_stg")
    df = df.withColumn("total_amount", col("quantity") * col("amount"))
    # df = df.withColumn("total_amount", expr("quantity * amount"))
    return df

# Create Empty Silver Streaming Table
dlt.create_streaming_table(
    name="sales_enr"
)

# Create Auto CDC Flow (AUTO CDC APIs replace the APPLY CHANGES APIs)
# https://docs.databricks.com/aws/en/dlt/cdc
dlt.create_auto_cdc_flow(
    target="sales_enr",
    source="sales_enr_view",
    keys=["sales_id"],
    sequence_by="sale_timestamp",
    ignore_null_updates=None,
    apply_as_deletes=None,
    apply_as_truncates=None,
    column_list=None,
    except_column_list=None,
    stored_as_scd_type=1,
    track_history_column_list=None,
    track_history_except_column_list=None
)