# Fraud Detection and Risk Analysis System

## Overview
This project is a rule-based fraud detection and risk analysis system designed to classify financial transactions into risk levels using data-driven thresholds.

## Objective
To demonstrate how data analysis techniques can be used to identify potentially fraudulent or high-risk financial transactions.

## Methodology
The system applies rule-based logic to transaction amounts:
- High Risk: ≥ 50,000,000
- Medium Risk: ≥ 10,000,000
- Low Risk: < 10,000,000

Each transaction is analyzed and assigned:
- Risk Level
- Fraud Reason
- Risk Score

## Tools Used
- Python
- Pandas

##  Output
The system generates a processed dataset (`risk_report.csv`) containing risk classifications and analysis results.

## How to Run
```bash
python fraud_detection.py
