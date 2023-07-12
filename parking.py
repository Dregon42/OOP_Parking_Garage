# Create at parking class
class Parking():

    # create __init__ method to store attributes
    def __init__(self, tickets, parking_spaces, current_tickets):
        self.tickets = tickets # <--list[]
        self.parking_spaces = parking_spaces # <-- list[]
        self.current_tickets = current_tickets # <-- dict{}


    # create method to decrase self.tickets & self.parking spaces by 1
    def takeTicket(self):
        day_pass = self.tickets.pop() 
        self.parking_spaces.pop()
        self.current_tickets[day_pass] = False
        print(f'Your ticket number: {day_pass}')

    # create method to pay for ticket
    # Display input asking to pay - store input in variable
    # if input not empty, give 15min response
    # update self.current_tickets (key = 'paid, value = True)
    def payForParking(self):
        tick_num = input('What is your ticket number ')
        if self.current_tickets[int(tick_num)] == False:
            payment = input("Pay here ")
            if payment != "":
                print('Ticket Paid for, you have 15mins to leave.')
                self.current_tickets[int(tick_num)] = True
            else:
                self.current_tickets[int(tick_num)] = False


    # create method for exiting garage
    # if ticket 'paid', display exit message
    # if not dipslay message for input, then display exit message
    # increase self.parking_spaces by 1
    # increase tickets by 1
    def leaveGarage(self):
        exit_num = input("Please enter ticket number. ")
        if self.current_tickets[int(exit_num)] == True: # Meaning ticket was paid for
            self.tickets.append(exit_num)          # add ticket back to list
            self.parking_spaces.append(exit_num)   # add spot back to parking_spaces
            print("Thank you have a nice day!")
        else:
            pay = input("Enter payment ") # if ticket is not paid for move to payForParking method
            print("Thank you have a nice day!") 


# Instantiate 
my_parkinglot = Parking([i for i in range(20)],[i for i in range(20)],{})


def run():

    i = 0

    while i < 20:
        response = input("Enter or Exit? ")
        if response.lower() == 'enter':
            my_parkinglot.takeTicket()
            my_parkinglot.payForParking()
            i += 1
        elif response.lower() == 'exit':
            my_parkinglot.leaveGarage()
            i -= 1
    return 'Parking lot is at capacity'

run()
