import great_expectations as gx

def main():
    context = gx.get_context()
    
    # Define datasource (adjust path as needed)
    datasource = context.sources.add_pandas_filesystem(
        name="local_parquet",
        base_directory="./data/processed"
    )

    # Create expectation suite if not exists
    suite_name = "parquet_quality_check"
    if not context.suites.has_suite(suite_name):
        context.suites.add(suite_name=suite_name)

    # Load data & run validation
    batch = datasource.get_asset("example.parquet").get_batch()
    validator = batch.validate(expectation_suite_name=suite_name)
    print(validator.get_statistics())

if __name__ == "__main__":
    main()
