class MemberInfo():
    
    def __init__(self):
        pass

    def add_new_member(self, name, address, emailId, phone):
        self.name = name
        self.address = address
        self.emailId = emailId
        self.phone = phone
        self.password = 'password'
        self.status = 'ACTIVE'
        self.uuid = self.generate_id() # We can create a seperate fun. to do this.

        #Write to database.
    
    def manage_memeber_account(self, uuid):
        # Be able to cancel or blacklist
        # Be able to issue a new card with same UUID.
        pass