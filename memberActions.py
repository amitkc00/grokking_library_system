from Person import MemberInfo

class MemberActions():
    
    def __init__(self, uuid):
        self.membershipId = uuid 
        # Assign PersonInfo here.

    def checkout_item(self):
        pass
    
    def checkin_item(self):
        pass
    
    def pay_fine(self):
        pass

    def manage_reservation(self):
        #" The user should be able to reserve / unreserve book" 
        pass

    def list_actions(self):
        print("1. Checkout Item")
        print("2. Checkin Item")
        print("3. Manage Reservation")
        print("4. Pay Fine")
        print("5. Exit")



    
    