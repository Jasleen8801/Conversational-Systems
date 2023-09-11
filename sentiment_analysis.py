from deephaven_server import Server
s = Server(port=3000, jvm_args=["-Xmx4g"])
s.start()

from deephaven import read_csv

sentiment = read_csv("https://media.githubusercontent.com/media/deephaven/examples/main/Sentiment/csv/sentiment.csv")
sentiment = sentiment.view(["text", "sentiment"]).where("sentiment != `Neutral`")
print(sentiment.head(5))