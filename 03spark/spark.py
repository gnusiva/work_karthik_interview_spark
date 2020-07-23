# from pyspark import SparkContext
# sc =SparkContext.getOrCreate()

# from pyspark.sql import SparkSession
# sess = SparkSession(sc)

# jdf = sess.read.json("../02filterData/filtered_data.json")
# jdf.withColumn('Date',jdf).show()

from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)

df = spark.read.json("../02filterData/filtered_data.json", multiLine=True)

df.printSchema()

