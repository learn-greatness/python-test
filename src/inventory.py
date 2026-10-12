def find_available_products(products, category=None, quantity=1): 
    """
    Return products that are available in the requested category and have
    enough stock.

    Product shape:
    {
        "id": 1,
        "name": "Ring",
        "category": "Rings",
        "stock": 5,
        "discontinued": False,
    }
    """
    if quantity <= 0:
        raise ValueError("quantity must be positive")

    result = []

    for product in products:
        if category is None or product["category"].lower() == category.lower():
            if product["stock"] >= quantity and not product["discontinued"]:
                result.append(product)

    
    return result
