import pymongo

connection_url = 'mongodb+srv://zubairrafi:zunaidahmedzaki37@cluster0.zuxy7id.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(connection_url)
  
# Database
Database = client.get_database('Store')