# Databricks notebook source
name = "race_results"
v_result = dbutils.notebook.run("1.race_results", 0, {"p_file_date": "2021-04-18","name":name})

# COMMAND ----------

global_temp_db = spark.conf.get("spark.sql.globalTempDatabase")
display(table(global_temp_db + "." + name))

# COMMAND ----------

name = "driver_standings"
v_result = dbutils.notebook.run("2.driver_standings", 0, {"p_file_date": "2021-04-18","name":name})

# COMMAND ----------

display(table(global_temp_db + "." + name))

# COMMAND ----------

name = "constructor_standings"
v_result = dbutils.notebook.run("3.constructor_standings", 0, {"p_file_date": "2021-04-18","name":name})

# COMMAND ----------

display(table(global_temp_db + "." + name))

# COMMAND ----------

name = "calculated_race_results"
v_result = dbutils.notebook.run("4.calculated_race_results", 0, {"p_file_date": "2021-04-18","name":name})
display(table(global_temp_db + "." + name))

# COMMAND ----------


