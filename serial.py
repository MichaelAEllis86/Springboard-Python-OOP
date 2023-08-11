
"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start=100):
        self.start=start
        self.next=start-1
    
    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        """ Generate the next number, increases by 1 for each time generate is used. """
        self.next += 1
        return self.next 
    
    def reset(self):
        """ Reset the generator so that the next generated number will be the original starting number"""
        self.next=self.start-1
        return f"serial generator reset to {self.start}"
    
    def print_current_number(self):
        """Prints/notifys the user what the current value of next is"""
        print(self.next)
    
    def print_next_serial(self):
        """ Prints/notifys the user what the next number produced by generate will be"""
        print(self.next + 1)
