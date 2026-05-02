CREATE TABLE [dbo].[sales_data] (

	[product_id] int NULL, 
	[customer_id] int NULL, 
	[transaction_id] int NULL, 
	[store_id] int NULL, 
	[quantity] int NULL, 
	[price] float NULL, 
	[timestamp] date NULL, 
	[name] varchar(8000) NULL, 
	[city] varchar(8000) NULL, 
	[segment] varchar(8000) NULL, 
	[category] varchar(8000) NULL, 
	[brand] varchar(8000) NULL
);