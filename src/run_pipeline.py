import random
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "data" / "input"
OUTPUT = BASE / "data" / "output"
INPUT.mkdir(parents=True, exist_ok=True)
OUTPUT.mkdir(parents=True, exist_ok=True)


def main():
    customers = pd.DataFrame([
        {
            "customer_id": f"CUST{i:05d}",
            "state": random.choice(["TX", "CA", "NY", "FL", "IL"]),
            "segment": random.choice(["RETAIL", "SMB", "ENTERPRISE"]),
            "signup_channel": random.choice(["web", "mobile", "branch"]),
        }
        for i in range(1, 501)
    ])

    transactions = pd.DataFrame([
        {
            "transaction_id": f"TXN{i:07d}",
            "customer_id": f"CUST{random.randint(1,500):05d}",
            "amount": round(random.uniform(10, 2500), 2),
            "merchant_category": random.choice(["retail", "travel", "grocery", "utilities"]),
        }
        for i in range(1, 3001)
    ])

    support = pd.DataFrame([
        {
            "ticket_id": f"TKT{i:06d}",
            "customer_id": f"CUST{random.randint(1,500):05d}",
            "ticket_type": random.choice(["billing", "technical", "account", "claim"]),
        }
        for i in range(1, 801)
    ])

    customers.to_csv(INPUT / "customers.csv", index=False)
    transactions.to_csv(INPUT / "transactions.csv", index=False)
    support.to_csv(INPUT / "support_tickets.csv", index=False)

    txn_features = transactions.groupby("customer_id", as_index=False).agg(
        transaction_count=("transaction_id", "count"),
        total_spend=("amount", "sum"),
        avg_transaction_amount=("amount", "mean"),
    )
    ticket_features = support.groupby("customer_id", as_index=False).agg(
        support_ticket_count=("ticket_id", "count")
    )

    mart = customers.merge(txn_features, on="customer_id", how="left").merge(ticket_features, on="customer_id", how="left")
    mart = mart.fillna({"transaction_count": 0, "total_spend": 0, "avg_transaction_amount": 0, "support_ticket_count": 0})
    mart.to_csv(OUTPUT / "customer_360_mart.csv", index=False)

    print("Customer 360 analytics mart completed")
    print(f"Output: {OUTPUT / 'customer_360_mart.csv'}")


if __name__ == "__main__":
    main()
