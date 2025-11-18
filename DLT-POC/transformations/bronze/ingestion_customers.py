import dlt

# Ingesting Customers
@dlt.table(name="customers_stg")
def customers_stg():
    df = spark.readStream.table("manib0906.source.customers")
    return df