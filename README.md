# 🏦 Bank Transfer System (ACID-Compliant)

A scalable and secure banking backend built with Python and SQLite, featuring interactive CLI operations, one-time data seeding, and Excel-based data exports. Designed to demonstrate core data engineering principles like atomic transactions, modular architecture, and realistic simulation.

---

## 🚀 Project Overview

This system allows users to create accounts, check balances, and perform fund transfers with **full ACID compliance**. It includes one-time bulk seeding of 1,000+ accounts using fake realistic data and exports all bank records to a human-readable Excel file for external inspection.

---

## 🔨 Features

### ✅ Account Management
- Create new accounts with auto-generated IDs
- Check account balances by ID
- View all accounts with names and balances

### 💸 Fund Transfers
- Atomic money transfers between accounts
- Prevents invalid transactions (e.g. non-existent IDs or insufficient balance)

### 🧪 Data Seeding
- Use [`faker`](https://faker.readthedocs.io/) to generate thousands of realistic client profiles
- Includes balances between 100.00–10,000.00
- Protected by one-time seeding flag (`seeding_status` table)

### 📤 Excel Export
- Export all account data to `bank_accounts.xlsx` using `pandas`
- Human-readable format for audits or import into PostgreSQL

### 🖥️ Command-Line Interface
- Create accounts, view balances, transfer funds interactively
- Includes option to list all users with ID + balance

---

## 🧱 Tech Stack

- **Python 3.11+**
- **SQLite** as lightweight embedded database
- **Faker** for data generation
- **Pandas + OpenPyXL** for Excel exports

---

## 📦 Installation

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


