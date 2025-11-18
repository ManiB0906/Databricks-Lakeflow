import dlt
from pyspark.sql.functions import col, expr
from pyspark.sql.types import *

# Create View to Encrich Data
@dlt.view(
    name="prodcuts_enr_view"
)
def prodcuts_enr_view():
    df = spark.readStream.table("products_stg")
    df = df.withColumn("price", col("price").cast(IntegerType()))
    df = df.withColumnRenamed("price", "amount")
    return df

# Create Empty Silver Streaming Table
dlt.create_streaming_table(
    name="products_enr"
)

# Create Auto CDC Flow (AUTO CDC APIs replace the APPLY CHANGES APIs)
# https://docs.databricks.com/aws/en/dlt/cdc
dlt.create_auto_cdc_flow(
    target="products_enr",
    source="prodcuts_enr_view",
    keys=["product_id"],
    sequence_by="last_updated",
    ignore_null_updates=None,
    apply_as_deletes=None,
    apply_as_truncates=None,
    column_list=None,
    except_column_list=None,
    stored_as_scd_type=1,
    track_history_column_list=None,
    track_history_except_column_list=None
)