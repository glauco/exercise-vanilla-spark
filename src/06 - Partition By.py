from pyspark.sql import *
import pyspark.sql.functions as F
from pyspark.sql.types import *
from lib.logger import Log4j
from config.definitions import DATA_DIR, OUTPUT_DIR

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Partitions App ->") \
        .getOrCreate()

    conf = spark.conf

    logger = Log4j(spark)

    logger.info("STARTED Partition By")

    # Paths
    temp_df = spark.read.format("csv").option("header", "true").load(f'{DATA_DIR}/country_data.csv')

    # Let's do a simple partition by, You will see a single partition in the job and all the data
    # will be written through on single out partition
    # temp_df.write.mode("overwrite").partitionBy("country").csv(f'{OUTPUT_DIR}/partition_by')

    # Let us now add repartition to the mix, now the default partitioner will come into picture
    temp_df.repartition(6).write.mode("overwrite").partitionBy("country")\
        .csv(f'{OUTPUT_DIR}/repartition_partition_by')

    input("Please ENTER")
    logger.info("FINISHED Partition By")
    spark.stop()


