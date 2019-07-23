from itemInfo import *

class LibraryItem():
    
    # Make it focused towards Books for now.
    def __init__(self):
        pass

    # Make it focused towards Books for now.
    def add_new_item(self, title, author, year, publisher):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.uuid = self.generate_id()
        self.status = 'AVAILABLE'
        self.lenderId = None # I think it is important to have this
        # information if we need to traceback a lender.
        # This is also a info. which changes with time and should be
        # kept seperate. Well, let's look into it more later.
    
    # Be able to remove this item from shelf, change
    # status to LOST, REFERENCE, RESERVED, OUT
    def manage_item(self, uuid):
        pass
    
