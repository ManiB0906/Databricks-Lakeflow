import dlt

# Expectations
products_expectations = {
    "rule1": "product_id is not NULL",
    "rule2": "price >= 0"
}

# Ingesting Products
@dlt.table(name="products_stg")
@dlt.expect_all_or_drop(products_expectations)
def products_stg():
    df = spark.readStream.table("manib0906.source.products")
    return df