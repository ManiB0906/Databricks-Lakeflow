import dlt
from pyspark.sql.functions import *

# Create Materialized Business View
@dlt.table(
    name="business_sales"
)
def business_sales():
    df_products = spark.read.table("products_dim")
    df_customers = spark.read.table("customers_dim")
    df_sales = spark.read.table("sales_fact")

    df_join = df_sales.join(df_customers, on="customer_id", how="inner").join(df_products, on="product_id", how="inner")

    df_prune = df_join.select("region", "category", "total_amount")

    df_agg = df_prune.groupBy("region", "category").agg(sum("total_amount").alias("total_sales"))

    return df_agg
    