from pyspark.streaming import StreamingContext
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Streaming")
sc = SparkContext.getOrCreate(conf = conf)
scc = StreamingContext(sc,1)

rdd = scc.textFileStream("directory")
rdd.map(lambda x: (x, 1))
rdd.reduceByKey(lambda x, y : x + y)
rdd.print()

scc.start()
scc.awaitTerminateOrTimeout(100) #10 seconds

# we can only have 1 spark context for streaming at the same time

# we need to restart the cluster to make it run again and release memory



