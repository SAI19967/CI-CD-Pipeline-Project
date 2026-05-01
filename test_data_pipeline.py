import pandas as pd
from src.data_pipeline import clean_data, transform_data


def test_clean_data_converts_numeric_columns():
    df = pd.DataFrame(
        {
            "Sales": ["100.5", "200.0"],
            "Profit": ["20.5", "30.0"],
            "Discount": ["0.1", "0.2"],
            "Category": [" Technology ", "Furniture"],
            "Sub_Category": [" Phones ", "Chairs"],
            "Region": [" East ", "West"],
        }
    )
    cleaned = clean_data(df)
    assert cleaned["Sales"].dtype == "float64"
    assert cleaned.loc[0, "Category"] == "Technology"


def test_transform_data_returns_category_summary():
    df = pd.DataFrame(
        {
            "Order_ID": ["1", "2", "3"],
            "Category": ["Technology", "Technology", "Furniture"],
            "Sales": [100.0, 200.0, 300.0],
            "Profit": [10.0, 20.0, 30.0],
            "Discount": [0.1, 0.2, 0.3],
        }
    )
    result = transform_data(df)
    assert "Total_Sales" in result.columns
    assert result[result["Category"] == "Technology"]["Total_Sales"].iloc[0] == 300.0
