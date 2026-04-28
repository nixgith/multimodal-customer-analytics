import pandas as pd
import random
from datetime import datetime, timedelta

print("Creating sample dataset...")

n = 5000
customers = [f'CUST{i:05d}' for i in range(1, 201)]
products = ['Wireless Earbuds', 'USB Cable', 'Phone Case', 'Screen Protector', 
            'Power Bank', 'Keyboard', 'Mouse', 'Laptop Stand', 'Monitor Arm', 'Webcam']

sentiments = [
    "Amazing product! Highly recommend!",
    "Great quality, fast shipping.",
    "Good value for money.",
    "Decent, but could be better.",
    "Not as described, disappointed.",
    "Waste of money, poor quality.",
    "Exactly what I needed!",
    "Works well, very satisfied.",
    "Broke after one week.",
    "Perfect! Will buy again."
]

base_date = datetime(2022, 1, 1)
dates = [base_date + timedelta(days=random.randint(0, 730)) for _ in range(n)]

df = pd.DataFrame({
    'customer_id': [random.choice(customers) for _ in range(n)],
    'product_id': [f'PROD{i}' for i in random.choices(range(1, 11), k=n)],
    'product_title': [random.choice(products) for _ in range(n)],
    'review_headline': [random.choice(sentiments) for _ in range(n)],
    'review_body': [random.choice(sentiments) + " " + random.choice(sentiments) for _ in range(n)],
    'star_rating': [random.choices([1, 2, 3, 4, 5], weights=[5, 10, 20, 35, 30])[0] for _ in range(n)],
    'helpful_votes': [random.randint(0, 50) for _ in range(n)],
    'total_votes': [random.randint(1, 100) for _ in range(n)],
    'verified_purchase': [random.choice(['Y', 'N']) for _ in range(n)],
    'review_date': [d.strftime('%Y-%m-%d') for d in dates],
})

df.to_csv('data/processed/sample_electronics_5k.csv', index=False)

print(f"✓ Created {len(df)} reviews")
print(f"✓ {df['customer_id'].nunique()} unique customers")
print(f"✓ {df['product_id'].nunique()} unique products")
print(f"\n✓ Saved to: data/processed/sample_electronics_5k.csv")