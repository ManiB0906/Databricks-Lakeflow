import dlt

# Create Empty Gold Streaming Table
dlt.create_streaming_table(
    name="sales_fact"
)

# Create Auto CDC Flow (AUTO CDC APIs replace the APPLY CHANGES APIs)
dlt.create_auto_cdc_flow(
    target="sales_fact",
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