from Person import *

class LibrarianActions():
    def __init__(self):
        pass 
    
    def manage_member_account(self):
        pass
    
    # Be able to checkout item on behalf of memebers.
    def checkout_item(self):
        pass
    
    def checkin_item(self):
        pass
    
    # Be able to process fine on  behalf of members
    def process_fine(self):
        pass

    # Add or Remove Books.
    def add_remove_items(self):
        pass
    
    # Be able to manage Reservations.
    # I finding it interesting to see how to work with same functions done by two different
    # kind of users. One with higher access than the other. Maybe UNIX permission style might
    # help here. To be continued.
    def manage_reservations(self):
        pass
    
    def list_actions(self):
        print("1. Manage Member Account")
        print("2. Checkout Item")
        print("3. Checkin Item")
        print("4. Manage Reservation")
        print("5. Process Fine")
        print("6. Add / Remove Items")
        print("5. Exit")

    



