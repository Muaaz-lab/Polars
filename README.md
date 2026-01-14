<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Polars DataFrame Explanation - Cafeteria Sales Scenario</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.7;
            background-color: #f4f6f8;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code, pre {
            background-color: #1e1e1e;
            color: #dcdcdc;
            padding: 10px;
            display: block;
            border-radius: 5px;
            overflow-x: auto;
        }
        .section {
            background-color: #ffffff;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 0 8px rgba(0,0,0,0.1);
        }
        ul {
            margin-left: 20px;
        }
    </style>
</head>

<body>

<h1>Using Polars Library for Cafeteria Sales Data Analysis</h1>

<div class="section">
    <h2>1. Introduction</h2>
    <p>
        This example demonstrates how the <strong>Polars</strong> library in Python is used to create
        and manage tabular data efficiently. Polars is a modern, high-performance DataFrame library
        designed as a faster alternative to Pandas, especially suitable for large datasets.
    </p>
    <p>
        In this scenario, we analyze <strong>cafeteria sales data</strong> collected over several days.
        Each record represents an item sold, the time of sale, quantity, and price.
    </p>
</div>

<div class="section">
    <h2>2. Importing the Polars Library</h2>
    <pre>
import polars as pl
    </pre>
    <p>
        Here, we import the Polars library using the alias <code>pl</code>.
        This alias is commonly used for convenience and readability in Polars-based projects.
    </p>
</div>

<div class="section">
    <h2>3. Creating the Dataset</h2>
    <pre>
data = {
    "day": ["Mon","Mon","Tue","Tue","Wed","Wed","Thu","Fri","Fri","Sat"],
    "item": ["Burger","Tea","Burger","Pizza","Tea","Burger","Pizza","Burger","Tea","Pizza"],
    "time": ["Morning","Morning","Afternoon","Evening","Morning","Evening",
             "Afternoon","Afternoon","Evening","Evening"],
    "quantity": [10,25,15,8,30,12,10,20,18,22],
    "price": [300,50,300,500,50,300,500,300,50,500]
}
    </pre>

    <p>
        The dataset is stored in a Python dictionary where:
    </p>
    <ul>
        <li><strong>day</strong> represents the day of the week.</li>
        <li><strong>item</strong> indicates the food or drink sold.</li>
        <li><strong>time</strong> shows when the item was sold (Morning, Afternoon, Evening).</li>
        <li><strong>quantity</strong> is the number of items sold.</li>
        <li><strong>price</strong> is the price per item (in local currency).</li>
    </ul>
    <p>
        Each key corresponds to a column, and each list represents the column values.
    </p>
</div>

<div class="section">
    <h2>4. Creating a Polars DataFrame</h2>
    <pre>
df = pl.DataFrame(data)
    </pre>
    <p>
        The <code>pl.DataFrame()</code> function converts the dictionary into a structured
        tabular format known as a <strong>DataFrame</strong>.
    </p>
    <p>
        A DataFrame organizes data into rows and columns, making it easy to analyze,
        filter, and transform.
    </p>
</div>

<div class="section">
    <h2>5. Displaying the DataFrame</h2>
    <pre>
print(df)
    </pre>
    <p>
        This line prints the DataFrame to the console.
        Polars automatically formats the output into a clean, readable table showing:
    </p>
    <ul>
        <li>Column names</li>
        <li>Data types</li>
        <li>All rows of data</li>
    </ul>
</div>

<div class="section">
    <h2>6. Why Polars is Used Here</h2>
    <ul>
        <li>Polars is significantly faster than Pandas.</li>
        <li>It uses efficient memory management.</li>
        <li>It supports parallel execution.</li>
        <li>Ideal for real-world data analytics scenarios.</li>
    </ul>
</div>

<div class="section">
    <h2>7. Real-World Use Case</h2>
    <p>
        This cafeteria sales dataset can later be used to:
    </p>
    <ul>
        <li>Identify best-selling items</li>
        <li>Analyze peak selling times</li>
        <li>Calculate daily or weekly revenue</li>
        <li>Optimize inventory and staffing decisions</li>
    </ul>
</div>

<div class="section">
    <h2>8. Conclusion</h2>
    <p>
        This example shows how simple it is to use Polars for structured data handling.
        With minimal code, we created a powerful and efficient DataFrame ready for
        further analysis.
    </p>
</div>

</body>
</html>
