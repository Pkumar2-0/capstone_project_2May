#!/usr/bin/env python
# coding: utf-8

# ## RetailX_Notebook
# 
# New notebook

# In[11]:


sales_df = spark.read.csv("Files/sales_data.csv", header=True, inferSchema=True)
customer_df = spark.read.csv("Files/customer_data.csv", header=True, inferSchema=True)
product_df = spark.read.csv("Files/product_data.csv", header=True, inferSchema=True)

sales_df.show()


# In[12]:


# Convert to RDD
rdd = sales_df.rdd

# Filter invalid records
rdd_filtered = rdd.filter(lambda x: x.quantity > 0 and x.price > 0)

# Map → (product_id, total_amount)
rdd_mapped = rdd_filtered.map(lambda x: (x.product_id, x.quantity * x.price))

# Reduce → total sales per product
rdd_reduced = rdd_mapped.reduceByKey(lambda a, b: a + b)

# Output
rdd_reduced.collect()


# In[13]:


from pyspark.sql.functions import col

# Clean data
clean_sales_df = sales_df.filter(
    (col("quantity") > 0) & (col("price") > 0)
)

# Add total column
clean_sales_df = clean_sales_df.withColumn(
    "total_amount",
    col("quantity") * col("price")
)

clean_sales_df.show()


# In[14]:


final_df = clean_sales_df \
    .join(customer_df, "customer_id") \
    .join(product_df, "product_id")

final_df.show()


# In[15]:


# Create temp view
final_df.createOrReplaceTempView("retail")

# SQL query
spark.sql("""
SELECT category, SUM(total_amount) AS total_sales
FROM retail
GROUP BY category
ORDER BY total_sales DESC
""").show()


# In[16]:


final_df.write.mode("overwrite").saveAsTable("retailx_sales")


# In[17]:


spark.sql("SHOW TABLES").show()

