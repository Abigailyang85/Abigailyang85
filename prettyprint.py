import pprint

shopping_platform = {
    "users": [
        {
            "user_id": 101,
            "username": "john_doe",
            "email": "john.doe@example.com",
            "address": {
                "street": "123 Elm St",
                "city": "Gotham",
                "zipcode": "12345",
                "country": "USA"
            },
            "order_history": [
                {
                    "order_id": 1001,
                    "order_date": "2025-04-10",
                    "total_amount": 250.75,
                    "items": [
                        {
                            "product_id": 201,
                            "name": "Laptop",
                            "quantity": 1,
                            "price": 999.99,
                            "discount": 0.1,  # 10% discount
                            "category": "electronics"
                        },
                        {
                            "product_id": 202,
                            "name": "Wireless Mouse",
                            "quantity": 1,
                            "price": 25.50,
                            "discount": 0.05,  # 5% discount
                            "category": "accessories"
                        }
                    ],
                    "shipping_details": {
                        "carrier": "FedEx",
                        "tracking_number": "ABC123456",
                        "delivery_date": "2025-04-12"
                    }
                }
            ]
        },
        {
            "user_id": 102,
            "username": "alice_smith",
            "email": "alice.smith@example.com",
            "address": {
                "street": "456 Oak St",
                "city": "Metropolis",
                "zipcode": "67890",
                "country": "Canada"
            },
            "order_history": [
                {
                    "order_id": 1002,
                    "order_date": "2025-04-11",
                    "total_amount": 145.30,
                    "items": [
                        {
                            "product_id": 203,
                            "name": "Headphones",
                            "quantity": 1,
                            "price": 89.99,
                            "discount": 0.15,  # 15% discount
                            "category": "electronics"
                        },
                        {
                            "product_id": 204,
                            "name": "Smartphone Case",
                            "quantity": 1,
                            "price": 19.99,
                            "discount": 0.1,  # 10% discount
                            "category": "accessories"
                        }
                    ],
                    "shipping_details": {
                        "carrier": "UPS",
                        "tracking_number": "XYZ987654",
                        "delivery_date": "2025-04-15"
                    }
                }
            ]
        }
    ],
    "products": {
        201: {
            "name": "Laptop",
            "category": "electronics",
            "brand": "TechBrand",
            "stock_quantity": 150,
            "price": 999.99,
            "discount": 0.1  # 10% discount
        },
        202: {
            "name": "Wireless Mouse",
            "category": "accessories",
            "brand": "ClickTech",
            "stock_quantity": 200,
            "price": 25.50,
            "discount": 0.05  # 5% discount
        },
        203: {
            "name": "Headphones",
            "category": "electronics",
            "brand": "SoundMax",
            "stock_quantity": 80,
            "price": 89.99,
            "discount": 0.15  # 15% discount
        },
        204: {
            "name": "Smartphone Case",
            "category": "accessories",
            "brand": "CaseCo",
            "stock_quantity": 300,
            "price": 19.99,
            "discount": 0.1  # 10% discount
        }
    },
    "inventory": {
        "electronics": {
            "laptops": 50,
            "headphones": 30
        },
        "accessories": {
            "mice": 70,
            "cases": 150
        }
    }
}


print(shopping_platform)
pprint.pprint(shopping_platform)
data = pprint.pformat(shopping_platform)
print(data)