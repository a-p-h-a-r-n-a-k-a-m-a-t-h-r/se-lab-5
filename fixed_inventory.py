"""
Inventory management system module.

This module provides functions to manage inventory stock data including
adding items, removing items, checking quantities, and persistence operations.
"""

import json
from datetime import datetime


# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.
    
    Args:
        item: Item name (str)
        qty: Quantity to add (int)
        logs: List to append log messages (optional)
    """
    if logs is None:
        logs = []
    
    if not item or not isinstance(item, str):
        return
    
    if not isinstance(qty, int) or qty < 0:
        return
    
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove an item from the inventory.
    
    Args:
        item: Item name (str)
        qty: Quantity to remove (int)
    """
    try:
        if item not in stock_data:
            raise KeyError(f"Item '{item}' not found in inventory")
        
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        print(f"Error removing item: {e}")


def get_qty(item):
    """
    Get the quantity of an item in inventory.
    
    Args:
        item: Item name (str)
        
    Returns:
        int: Quantity of the item
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.
    
    Args:
        file: Path to the JSON file (str)
    """
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with empty inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.
    
    Args:
        file: Path to the JSON file (str)
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=2)


def print_data():
    """Print a report of all items in inventory."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """
    Check for items below a threshold quantity.
    
    Args:
        threshold: Minimum quantity threshold (int)
        
    Returns:
        list: Items below the threshold
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory system usage."""
    add_item("apple", 10)
    add_item("banana", 5)
    # Invalid type calls now handled by validation
    add_item(123, "ten")  # Will be rejected by type checking
    
    remove_item("apple", 3)
    remove_item("orange", 1)  # Will handle gracefully
    
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    
    save_data()
    load_data()
    print_data()
    
    # Replaced dangerous eval with safe alternative
    print('Diagnostic message printed safely')


if __name__ == "__main__":
    main()
