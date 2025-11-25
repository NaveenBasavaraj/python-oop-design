# Simple Bank System - Low Level Design (LLD)

## Overview

This document explains the Low Level Design (LLD) of a simple bank system using clean OOP principles.

---

# 1. Entities

## **1. Bank**

Manages all customers and accounts. Responsible for opening accounts and transferring money.

```
+----------------+
|     Bank       |
+----------------+
| - customers    |
| - accounts     |
+----------------+
| + createCustomer() |
| + openAccount()    |
| + transfer()       |
+----------------+
```

---

## **2. Customer**

Represents a user of the bank.

```
+----------------+
|   Customer     |
+----------------+
| customer_id    |
| name           |
| email          |
+----------------+
| + addAccount() |
| + getBalance() |
+----------------+
```

---

## **3. Account (Abstract Base Class)**

```
+---------------------+
|      Account        |
+---------------------+
| account_number      |
| owner_id            |
| balance             |
+---------------------+
| + deposit()         |
| + withdraw()        |
| + can_withdraw() *  |
+---------------------+
```

---

## **4. SavingsAccount**

```
+--------------------------+
|     SavingsAccount       |
+--------------------------+
| inherits Account         |
+--------------------------+
| + can_withdraw()         |
+--------------------------+
```

---

## **5. CurrentAccount**

```
+--------------------------+
|     CurrentAccount       |
+--------------------------+
| overdraft_limit          |
+--------------------------+
| + can_withdraw()         |
+--------------------------+
```

---

## **6. Transaction**

```
+--------------------+
|    Transaction     |
+--------------------+
| timestamp          |
| amount             |
| type               |
| description        |
+--------------------+
```

---

# 2. Entity Relationship Diagram

```
       +--------+
       |  Bank  |
       +--------+
           |
           v
     +------------+
     |  Customer  |
     +------------+
           |
           v
     +------------+
     |  Account   |<-----------------+
     +------------+                  |
      /          \                  |
     v            v                  |
+-----------+  +--------------+      |
| Savings   |  |  Current     |      |
| Account   |  |  Account     |      |
+-----------+  +--------------+      |
           \_________               |
                     \              |
                      v             |
                +----------+        |
                |Transaction|<------+
                +----------+
```

---

# 3. Design Patterns Used

### **Template Method**

- `Account.withdraw()` → algorithm is fixed
- Subclasses override `can_withdraw()`

### **Inheritance**

SavingsAccount, CurrentAccount → inherit Account.

### **Composition**

Bank → Customers → Accounts → Transactions.

---

# 4. Flow Summary

1. Bank creates a customer.
2. Customer gets savings/current accounts.
3. Deposits & withdrawals trigger Transaction logs.
4. Transfer = withdraw(from) + deposit(to).

---

# 5. Conclusion

A clean, extendable, modular system perfect for teaching OOP & LLD.
