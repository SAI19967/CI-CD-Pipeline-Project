import pandas as pd
import pytest
from src.data_quality import (
    validate_required_columns,
    validate_no_nulls,
    validate_sales_values,
    validate_discount_range,
)


def sample_df():
    return pd.DataFrame(
        {
            "Order_ID": ["CA-1001", "CA-1002"],
            "Customer_Name": ["John Smith", "Sarah Jones"],
            "Category": ["Technology", "Furniture"],
            "Sub_Category": ["Phones", "Chairs"],
            "Sales": [1200.50, 650.00],
            "Profit": [250.75, 80.25],
            "Discount": [0.10, 0.15],
            "Region": ["East", "West"],
            "City": ["New York", "Los Angeles"],
        }
    )


def test_validate_required_columns_success():
    df = sample_df()
    assert validate_required_columns(df, ["Order_ID", "Sales", "Profit"]) is True


def test_validate_required_columns_failure():
    df = sample_df()
    with pytest.raises(ValueError):
        validate_required_columns(df, ["Order_ID", "Missing_Column"])


def test_validate_no_nulls_success():
    df = sample_df()
    assert validate_no_nulls(df, ["Order_ID", "Sales"]) is True


def test_validate_sales_values_failure():
    df = sample_df()
    df.loc[0, "Sales"] = -100
    with pytest.raises(ValueError):
        validate_sales_values(df)


def test_validate_discount_range_failure():
    df = sample_df()
    df.loc[0, "Discount"] = 2.5
    with pytest.raises(ValueError):
        validate_discount_range(df)
