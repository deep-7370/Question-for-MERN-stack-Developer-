import requests
from .models import ProductTransaction
from django.db import transaction

class DatabaseInitializationService:
    @classmethod
    def initialize_database(cls):
        try:
            # Fetch data from third-party API
            response = requests.get('https://s3.amazonaws.com/roxiler.com/product_transaction.json')
            transactions = response.json()

            # Bulk create transactions with error handling
            with transaction.atomic():
                product_transactions = [
                    ProductTransaction(
                        title=item.get('title', ''),
                        description=item.get('description', ''),
                        price=item.get('price', 0),
                        category=item.get('category', ''),
                        image=item.get('image', ''),
                        sold=item.get('sold', False),
                        dateOfSale=item.get('dateOfSale', timezone.now())
                    ) for item in transactions
                ]
                ProductTransaction.objects.bulk_create(product_transactions)

            return len(product_transactions)
        
        except requests.RequestException as e:
            print(f"API Request Error: {e}")
            return 0
        except Exception as e:
            print(f"Initialization Error: {e}")
            return 0