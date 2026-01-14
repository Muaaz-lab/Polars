import polars as pl

data = {
    "day": ["Mon","Mon","Tue","Tue","Wed","Wed","Thu","Fri","Fri","Sat"],
    "item": ["Burger","Tea","Burger","Pizza","Tea","Burger","Pizza","Burger","Tea","Pizza"],
    "time": ["Morning","Morning","Afternoon","Evening","Morning","Evening","Afternoon","Afternoon","Evening","Evening"],
    "quantity": [10,25,15,8,30,12,10,20,18,22],
    "price": [300,50,300,500,50,300,500,300,50,500]
}

df = pl.DataFrame(data)
print(df)
df = df.with_columns(
    (pl.col("quantity") * pl.col("price")).alias("revenue")
)

print(df)
most_sold = (
    df.group_by("item")
      .agg(pl.col("quantity").sum().alias("total_sold"))
      .sort("total_sold", descending=True)
)

print(most_sold)
time_revenue = (
    df.group_by("time")
      .agg(pl.col("revenue").sum().alias("total_revenue"))
      .sort("total_revenue", descending=True)
)

print(time_revenue)
best_day = (
    df.group_by("day")
      .agg(pl.col("revenue").sum().alias("daily_revenue"))
      .sort("daily_revenue", descending=True)
)

print(best_day)
