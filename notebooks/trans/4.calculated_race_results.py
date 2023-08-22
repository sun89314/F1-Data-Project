# Databricks notebook source
dbutils.widgets.text("p_file_date", "2021-03-21")
dbutils.widgets.text("name","race_results") 
v_file_date = dbutils.widgets.get("p_file_date")
name = dbutils.widgets.get("name")

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

# MAGIC %run "../includes/configuration"

# COMMAND ----------

# MAGIC %run "../includes/common_functions"

# COMMAND ----------

# %sql
# CREATE TABLE f1_presentation.calculated_race_results
# USING parquet
# AS
# SELECT races.race_year,
#        constructors.name AS team_name,
#        drivers.name AS driver_name,
#        results.position,
#        results.points,
#        11 - results.position AS calculated_points
#   FROM results 
#   JOIN f1_processed.drivers ON (results.driver_id = drivers.driver_id)
#   JOIN f1_processed.constructors ON (results.constructor_id = constructors.constructor_id)
#   JOIN f1_processed.races ON (results.race_id = races.race_id)
#  WHERE results.position <= 10

# COMMAND ----------

race_results_df = spark.read.parquet(f"{presentation_folder_path}/race_results") \
.filter(f"file_date = '{v_file_date}'") 
# drivers_df = spark.read.parquet(f"{processed_folder_path}/drivers") 
# constructors_df = spark.read.parquet(f"{processed_folder_path}/constructors") 
# races_df = spark.read.parquet(f"{processed_folder_path}/races") 

# COMMAND ----------

display(race_results_df)

# COMMAND ----------

top10_df = race_results_df.filter('position < 10')
final_df = top10_df.select(top10_df.race_year,top10_df.race_name,top10_df.driver_name,top10_df.position,top10_df.points)\
  .withColumn('calculated_points',11 - col('position'))
display(final_df)  

# COMMAND ----------

final_df.write.mode("overwrite").format("parquet").saveAsTable("f1_presentation.calculated_race_results")
# overwrite_partition(final_df, 'f1_presentation', 'calculated_race_results', 'race_year')

# COMMAND ----------



# COMMAND ----------

final_df.createOrReplaceGlobalTempView(name)
dbutils.notebook.exit(name)

# COMMAND ----------


