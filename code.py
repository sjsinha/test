words= sc.textFile("file:///C:/Users/surya/OneDrive/Desktop/xyz.txt").flatMap(lambda line: line.split(" "))
a=words.map(lambda word: (word,1))
b=a.reduceByKey(lambda a,b:a +b)

