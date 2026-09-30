# main.py
from datetime import date
from auth import login, register
from tracker import log_food
from analytics import show_daily_summary
from ai_service import client

def main():
    if not client:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set it before running the tracker.")
        return

    current_user = None
    
    while True:
        if not current_user:
            choice = input("\n1. Login\n2. Register\n3. Exit\nSelect option: ")
            if choice == '1':
                current_user = login()
            elif choice == '2':
                current_user = register()
            elif choice == '3':
                break
            else:
                print("Invalid input.")
        else:
            choice = input("\n1. Log Food\n2. View Today's Summary\n3. Logout\nSelect option: ")
            if choice == '1':
                log_food(current_user)
            elif choice == '2':
                show_daily_summary(current_user, str(date.today()))
            elif choice == '3':
                current_user = None
                print("Logged out.")
            else:
                print("Invalid input.")

if __name__ == "__main__":
    main()