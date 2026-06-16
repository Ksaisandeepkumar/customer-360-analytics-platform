# Customer 360 Analytics Platform

## Business Problem
Organizations need a unified customer view across profile, transaction, support, and engagement data. Siloed datasets make it difficult to understand customer behavior and operational risk.

## Objective
Build a Customer 360 analytics mart that integrates customer attributes, transaction features, and support ticket activity.

## Architecture
```text
Customer Data + Transactions + Support Tickets
  -> Feature Engineering
  -> Customer 360 Mart
```

## Key Data Engineering Concepts
- Entity-level feature engineering
- Customer dimensional modeling
- Multi-source joins
- Analytics-ready mart creation

## How to Run
```bash
python src/run_pipeline.py
```

## Resume Bullet
Built a Customer 360 analytics platform that integrates profile, transaction, and support datasets into a single customer-level mart with spend, activity, and service metrics.
