def validate_data(df):
    """Validate that the generated data meets certain rules."""
    assert df["Registration ID"].is_unique, "Unique keys are not unique."
    assert df["Annual Revenue (USD)"].between(0, 1200000000).all(), "Annual revenue must be between 0 and 1,200,000,000."
    assert df["Employee Satisfaction Index (1-10)"].between(1, 10).all(), "Employee satisfaction must be between 1 and 10."