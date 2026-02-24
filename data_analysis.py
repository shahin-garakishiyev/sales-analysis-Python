from data_read import read_data
from data_clean import clean_data


def calculate_kpis(df):
    """
    Calculates core company KPIs
    """
    total_revenue = df["Revenue"].sum()
    total_profit = df["Net_profit"].sum()

    return total_revenue, total_profit


def analyze_products(df):
    """
    Identifies top profitable products
    """
    return df.groupby("Product_name")["Net_profit"] \
            .sum() \
            .sort_values(ascending=False) \
            .head()


def analyze_regions(df):
    """
    Regional performance analysis
    """
    return df.groupby("Region_name")["Revenue"] \
            .sum() \
            .sort_values(ascending=False)


def analyze_promotions(df):
    """
    Promotion performance impact
    """
    return df.groupby("Promotion_flag")["Revenue"].mean()


def time_analysis(df):
    """
    Revenue analysis by weekday
    """
    order = ["Monday", "Tuesday", "Wednesday", "Thursday",
             "Friday", "Saturday", "Sunday"]

    weekly = df.groupby("Weekday")["Revenue"].sum().reindex(order)

    return weekly


def weekend_analysis(df):
    """
    Weekday vs Weekend revenue comparison
    """
    return df.groupby("Day_type")["Revenue"].sum()


def correlation_analysis(df):
    """
    Correlation analysis between key numerical variables
    """
    return df[["Revenue", "Net_profit", "Product_count", "Price"]].corr()


def main():

    # 1. Read Data
    sales = read_data()

    # 2. Clean Data
    sales = clean_data(sales)

    # 3. KPI Report
    total_revenue, total_profit = calculate_kpis(sales)

    print("\n=== COMPANY KPI REPORT ===")
    print(f"Total Revenue: {total_revenue:,.2f}")
    print(f"Total Profit: {total_profit:,.2f}")

    # 4. Product Analysis
    print("\n=== TOP PRODUCTS BY PROFIT ===")
    print(analyze_products(sales))

    # 5. Regional Analysis
    print("\n=== REGIONAL PERFORMANCE ===")
    print(analyze_regions(sales))

    # 6. Promotion Analysis
    print("\n=== PROMOTION PERFORMANCE ===")
    print(analyze_promotions(sales))

    # 7. Time-Based Analysis
    print("\n=== DAILY REVENUE ANALYSIS ===")
    print(time_analysis(sales))
    
    print("\n=== WEEKDAY VS WEEKEND REVENUE ===")
    print(weekend_analysis(sales))

    # 8. Correlation Analysis
    print("\n=== CORRELATION MATRIX ===")
    print(correlation_analysis(sales))


if __name__ == "__main__":
    main()