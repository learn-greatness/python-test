# Python & Backend Readiness Coding Test

Welcome.

This repository is a small Python project containing some broken code and some incomplete features.

Your job is to **read the existing code, understand what it is supposed to do, fix the problems, and make the tests pass.**

This is not a DSA test.

You do not need advanced algorithms. We are mainly interested in whether you can:

* understand Python code written by someone else;
* find and fix bugs;
* write simple functions;
* work with lists and dictionaries;
* handle normal and unusual inputs;
* write basic tests;
* explain why your code works.

---

# Before You Start

Do not immediately start changing code.

Use this process whenever you work on a task:

```text
1. Read the task
       ↓
2. Run the tests
       ↓
3. Look at the error
       ↓
4. Open the relevant Python file
       ↓
5. Understand what the current code is doing
       ↓
6. Find the problem
       ↓
7. Make a small change
       ↓
8. Run the tests again
       ↓
9. Check whether there are other cases you should test
```

You are allowed to use:

* Python documentation
* `print()` for debugging
* a debugger
* the terminal
* the existing tests

You should **not** use AI/code-generation tools for this assessment.

Do not rewrite the entire project.

Try to change only the code that actually needs to be changed.

---

# Setup

You need Python 3.11 or newer.

First, run:

```bash
python -m pytest
```

If `pytest` is not installed, use:

```bash
python -m unittest discover -s tests -v
```

You should see some tests failing.

**That is expected.**

The repository intentionally contains bugs.

Your job is to make the code behave according to the requirements below.

---

# Task 1 — Fix the Order Total

### File

```text
src/order_utils.py
```

### Function

```python
calculate_order_total(order)
```

This function calculates how much a customer needs to pay for an order.

An order looks like this:

```python
order = {
    "items": [
        {"price": 100, "quantity": 2},
        {"price": 50, "quantity": 1}
    ],
    "discount_percent": 10,
    "tax_percent": 18
}
```

For this order, calculate the total like this.

### Step 1 — Calculate each item's price

The first item costs:

```text
100 × 2 = 200
```

The second item costs:

```text
50 × 1 = 50
```

So the subtotal is:

```text
200 + 50 = 250
```

### Step 2 — Apply the discount

The discount is 10%.

10% of 250 is:

```text
25
```

So after the discount:

```text
250 - 25 = 225
```

### Step 3 — Apply tax

The tax is 18%.

18% of 225 is:

```text
40.50
```

So the final total is:

```text
225 + 40.50 = 265.50
```

Therefore:

```python
calculate_order_total(order)
```

should return:

```python
265.50
```

### Your job

Open `src/order_utils.py` and fix the function so that it follows the calculation above.

Also make sure:

* `quantity` is actually used when calculating an item's price;
* the discount is treated as a percentage;
* tax is calculated after the discount;
* the returned value is rounded to 2 decimal places;
* the original `order` dictionary is not changed.

You do **not** need to redesign the function.

Start by running the tests and then reading the existing implementation carefully.

---

# Task 2 — Fix Product Search

### File

```text
src/inventory.py
```

### Function

```python
find_available_products(products, category=None, quantity=1)
```

This function receives a list of products and should return the products that are available to buy.

A product looks like:

```python
{
    "id": 1,
    "name": "Silver Ring",
    "category": "Rings",
    "stock": 5,
    "discontinued": False
}
```

Suppose we have:

```python
products = [
    {
        "id": 1,
        "name": "Silver Ring",
        "category": "Rings",
        "stock": 5,
        "discontinued": False
    },
    {
        "id": 2,
        "name": "Gold Ring",
        "category": "Rings",
        "stock": 0,
        "discontinued": False
    },
    {
        "id": 3,
        "name": "Old Ring",
        "category": "Rings",
        "stock": 10,
        "discontinued": True
    }
]
```

If we ask:

```python
find_available_products(products, "Rings", 2)
```

only the first product should be returned.

Why?

```text
Silver Ring
stock = 5
requested = 2
available = yes

Gold Ring
stock = 0
requested = 2
available = no

Old Ring
discontinued = yes
available = no
```

### Your job

Fix the function so that a product is returned only when:

1. It belongs to the requested category.
2. It has enough stock.
3. It is not discontinued.

Category names should not care about uppercase/lowercase.

For example:

```python
"Rings"
```

and:

```python
"rings"
```

should be treated as the same category.

Also:

* if `quantity` is invalid, raise `ValueError`;
* do not modify the original `products` list;
* the product's name should not affect whether it is returned.

You do not need to sort the products unless the existing tests/requirements require it.

---

# Task 3 — Calculate Order Statistics

### File

```text
src/analytics.py
```

This task is different from the first two.

The function is currently incomplete.

You need to implement:

```python
summarize_orders(orders)
```

Each order looks like:

```python
{
    "id": 1,
    "status": "completed",
    "total": 100.50
}
```

Possible statuses are:

```text
completed
cancelled
pending
```

Suppose we have:

```python
orders = [
    {"id": 1, "status": "completed", "total": 100},
    {"id": 2, "status": "completed", "total": 50},
    {"id": 3, "status": "cancelled", "total": 200},
    {"id": 4, "status": "pending", "total": 300}
]
```

The function should return:

```python
{
    "total_orders": 4,
    "completed_orders": 2,
    "cancelled_orders": 1,
    "total_revenue": 150,
    "average_order_value": 75
}
```

Why?

There are 4 orders total.

2 are completed.

1 is cancelled.

Only completed orders generate revenue:

```text
100 + 50 = 150
```

The average completed order value is:

```text
150 / 2 = 75
```

Cancelled and pending orders do not contribute to revenue.

### Your job

Implement the function.

Make sure:

* `total_orders` counts every order;
* `completed_orders` counts only completed orders;
* `cancelled_orders` counts only cancelled orders;
* only completed orders contribute to revenue;
* `average_order_value` uses completed orders;
* if there are no completed orders, the average should be `0`;
* an empty list should work;
* the original list should not be changed;
* revenue and average should be rounded to 2 decimal places.

Start by looking at the existing file and the existing tests.

---

# Task 4 — Validate a User

### File

```text
src/validation.py
```

### Function

```python
validate_user(user)
```

This function checks whether a user contains valid basic information.

A valid user looks like:

```python
{
    "name": "Alice",
    "email": "alice@example.com",
    "age": 22
}
```

A user is valid when:

### Name

The name must be a non-empty string.

This is invalid:

```python
{"name": "", ...}
```

This is also invalid:

```python
{"name": 123, ...}
```

### Email

For this exercise, an email is considered valid if it contains **exactly one `@`**.

For example:

```text
alice@example.com
```

is valid.

But:

```text
aliceexample.com
```

is invalid.

You do not need to build a complete email validation system.

### Age

The age must be an integer between:

```text
13 and 120
```

inclusive.

So:

```text
13 → valid
22 → valid
120 → valid
12 → invalid
121 → invalid
```

### Invalid input

For invalid input, raise:

```python
ValueError
```

with a useful message.

If required information is missing, also raise `ValueError`.

Do not modify the original user dictionary.

### Your job

Implement/fix `validate_user()` so that it follows the rules above.

Do not worry about advanced validation or regular expressions.

Keep the solution simple.

---

# Task 5 — Fix the Order Service

### File

```text
src/service.py
```

This is a very small example of something that could eventually become part of a backend application.

There is an `OrderService` class.

Orders are stored in memory using Python.

You need to fix/complete three operations:

```python
create_order(user_id, items)
get_order(order_id)
cancel_order(order_id)
```

---

## 5.1 Create an order

Example:

```python
service.create_order(
    10,
    [
        {"product_id": 5, "quantity": 2}
    ]
)
```

should create an order similar to:

```python
{
    "id": 1,
    "user_id": 10,
    "items": [
        {"product_id": 5, "quantity": 2}
    ],
    "status": "pending"
}
```

The exact ID depends on which orders have already been created.

### Requirements

* `user_id` must be a positive integer.
* There must be at least one item.
* Every item must contain a `product_id`.
* Every item must contain a positive integer `quantity`.
* Every newly created order starts as `"pending"`.
* Every order needs a unique ID.
* The created order should be stored.
* Return the created order.

---

## 5.2 Get an order

This should:

```python
service.get_order(order_id)
```

return the order if it exists.

If the order doesn't exist, raise:

```python
OrderNotFoundError
```

For example:

```python
service.get_order(999)
```

should raise the exception if order `999` doesn't exist.

---

## 5.3 Cancel an order

An order can be cancelled.

For example:

```text
pending → cancelled
```

After cancellation, its status should be:

```python
"cancelled"
```

However, a completed order cannot be cancelled.

If someone tries to cancel a completed order, raise:

```python
InvalidOrderStateError
```

Also, don't silently allow an already-cancelled order to transition into some other invalid state.

### Your job

Read the existing `OrderService` implementation carefully.

Some of the behavior is already present, but it is incorrect/incomplete.

Fix it so that it follows the rules above.

You do not need to add a database, web server, API, or framework.

This is just a Python class storing data in memory.

---

# Task 6 — Write Your Own Tests

After fixing the previous tasks, write some tests yourself.

Add at least **4 tests**.

Your tests should include different kinds of situations.

For example:

* a normal input;
* an empty input;
* invalid input;
* a boundary value;
* an object that doesn't exist;
* a state that shouldn't be allowed.

Do not simply duplicate the existing tests.

The purpose of this task is to show that you can think:

> "What else could go wrong?"

---

# Create `ANSWERS.md`

Create a file called:

```text
ANSWERS.md
```

Answer these questions in your own words.

You do not need long answers.

### 1.

What is the difference between:

```text
list
tuple
set
dictionary
```

### 2.

What is the difference between:

```python
==
```

and:

```python
is
```

### 3.

What happens if a list is passed into a function and the function changes that list?

### 4.

What is the difference between:

```python
return
break
continue
```

### 5.

What is an exception?

Why do we use exceptions instead of allowing the program to continue with bad data?

### 6.

What happens here?

```python
x = [1, 2, 3]
y = x

y.append(4)

print(x)
print(y)
```

Explain why.

### 7.

What happens here?

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))
print(add_item("b"))
```

Explain why.

### 8.

What is the difference between a function returning:

```python
None
```

and:

```python
[]
```

### 9.

Why should a backend application validate user input before storing it?

---

# When You Are Finished

Run all tests again:

```bash
python -m pytest
```

or:

```bash
python -m unittest discover -s tests -v
```

Make sure your tests pass.

Then check your changes with:

```bash
git diff
```

You should be able to explain every change you made.

You do not need to make the code complicated.

**Simple, understandable code is preferred.**

---

# What We Are Looking For

We are not only looking at whether the final tests pass.

We also care about how you solve the problems.

Good signs include:

* reading the existing code before changing it;
* running the tests;
* reading error messages carefully;
* using small changes;
* checking your work after making a change;
* thinking about edge cases;
* writing useful tests;
* being able to explain your solution.

If you get stuck, don't immediately rewrite everything.

Go back to the process:

```text
What should happen?
        ↓
What is actually happening?
        ↓
Where in the code does that happen?
        ↓
What small change would make the behavior correct?
```

The purpose of this exercise is not to know everything.

It is to see how you approach a problem you have not seen before.
