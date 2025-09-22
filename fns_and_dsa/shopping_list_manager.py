#!/usr/bin/env python3
"""
Shopping List Manager
A simple program to manage a shopping list using Python lists
"""


def display_menu():
    """Display the main menu options"""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """Main function to run the shopping list manager"""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add item functionality
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item cannot be empty. Please enter a valid item name.")
                
        elif choice == '2':
            # Remove item functionality
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue
                
            print("Current shopping list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
                
            item_to_remove = input("Enter the item to remove: ").strip()
            
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from your shopping list.")
            else:
                print(f"'{item_to_remove}' was not found in your shopping list.")
                
        elif choice == '3':
            # View list functionality
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                print("-" * 20)
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("-" * 20)
                
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
