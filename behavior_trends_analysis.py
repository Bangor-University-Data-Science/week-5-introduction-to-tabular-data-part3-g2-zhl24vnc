import pandas as pd

def import_data(filename: str) -> pd.DataFrame:
    if filename.endswith('.xlsx'):
        return pd.read_excel(filename)
    elif filename.endswith('.csv'):
        return pd.read_csv(filename)
    else:
        raise ValueError("Unsupported file format.")

def filter_data(df: pd.DataFrame):
    df = df.dropna(subset=['CustomerID'])
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    return df

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    return df[df['CustomerID'].isin(df.groupby('CustomerID').size()[lambda x: x >= min_purchases].index)]

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    return df.resample('Q', on='InvoiceDate').agg({'Revenue': 'sum'}).reset_index().rename(columns={'Revenue': 'total_revenue'})

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    return df.groupby('StockCode').agg({'Quantity': 'sum'}).nlargest(top_n, 'Quantity').reset_index()

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('StockCode').agg({'Quantity': 'mean', 'UnitPrice': 'mean'}).reset_index().rename(columns={'Quantity': 'avg_quantity', 'UnitPrice': 'avg_unit_price'})

def answer_conceptual_questions() -> dict:
    return {
        "Q1": {"A", "C"},
        "Q2": {"B"},
        "Q3": {"A", "C"},
        "Q4": {"A", "B"},
        "Q5": {"A"}
    }