from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

class DB_operation:

    def __init__(self):
        self.id = "tPebElScFgGZjhusPvJdZwsi"
        self.secret = "TWn.rZCke5tvP7OAZH1mq6gkfrS_hCeKfTFto.qnFjaZ4I-E_Yrey6yDP5tGscFJf03-c+I.9RmJJcjojpcWj9l,MPK.SjHoAgSpePURoraE-z9mmfJYMzHhRdGslO,d"
        self.path = "D:\Full Stack Data Science\Python Project\Review Scrapper\Basic_Flipkart_Review_Scrapper\secure-connect-basic-flipkart-web-scrapper.zip"
        self.keyspace = "basic_scrapper"
        self.client = None

    def create_session(self):
        cloud_config = {self.path}
        auth_provider = PlainTextAuthProvider(self.id, self.secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()

    def create_table(self, table_name, columns):
        self.session.execute(f"create table {table_name}('{columns[0]}' text, '{columns[1]}' text, '{columns[2]}' text, '{columns[3]}' text, '{columns[4]}' text);")

    def insert_record(self, table_name, columns, record):
        self.session.execute(f"insert into table({columns[0]}, {columns[1]}, {columns[2]}, {columns[3]}, {columns[4]}) values({record[columns[0]]}, {record[columns[1]]}, {record[columns[2]]}, {record[columns[3]]}, {record[columns[4]]});")

    def delete_record(self, collection):
        rec = collection.find().sort({'_id':-1}).limit(1)
        collection.delete_one(rec)

# f = open(r"D:\Full Stack Data Science\Python Project\Review Scrapper\Basic_Flipkart_Review_Scrapper\secure-connect-basic-flipkart-web-scrapper.zip", 'r')
# cloud_config = r"D:\Full Stack Data Science\Python Project\Review Scrapper\Basic_Flipkart_Review_Scrapper\secure-connect-basic-flipkart-web-scrapper.zip"
# auth_provider = PlainTextAuthProvider("tPebElScFgGZjhusPvJdZwsi", "TWn.rZCke5tvP7OAZH1mq6gkfrS_hCeKfTFto.qnFjaZ4I-E_Yrey6yDP5tGscFJf03-c+I.9RmJJcjojpcWj9l,MPK.SjHoAgSpePURoraE-z9mmfJYMzHhRdGslO,d")
# cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
# session = cluster.connect()