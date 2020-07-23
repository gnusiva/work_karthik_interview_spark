

from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)

path = '../02filterData/filtered_data.json'
df = spark.read.json(path, multiLine=True)

df.write.format("jdbc").options(url ="jdbc:sqlite:test.db", driver="org.sqlite.JDBC", dbtable="DailyExchange").save()
# df.printSchema()
# df.show()

