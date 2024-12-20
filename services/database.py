from mongoengine import connect
from config.settings import Settings

class DatabaseService:
    def __init__(self):
        self.settings = Settings()
        self.db = None

    def connect(self):
        try:
            self.db = connect(host=self.settings.DATABASE_URL)
            print("Connected to the database successfully.")
        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")

    def disconnect(self):
        if self.db:
            self.db.close()
            print("Disconnected from the database.")

database_service = DatabaseService()

