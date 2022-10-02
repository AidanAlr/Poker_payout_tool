
# Player class containing information about the game
class Player:
    def __init__(self, name, buyin, cashout):
        self.name = name
        self.buyin = buyin
        self.cashout = cashout
        self.net = cashout - buyin

# Function for calculating the payouts
def calculate_payouts(participants):

    # Sorting the payouts from largest[0] to smallest[-1]
    participants.sort(key=lambda Player: Player.net, reverse=True)

    # Payout Table
    print('Payouts:'.upper())
    for person in participants:
        print(f'{person.name} = {person.net}')

    print('\n')
    print('Payout calculator:'.upper())

    # Calculating who pays whom starting with the largest loss and largest winner
    # While there are still participants i.e. those that need to be paid out
    while participants:
        try:
            # If largest win greater than absolute largest loss
            if participants[0].net > abs(participants[-1].net):
                # Print that payout
                print(f'{participants[-1].name} pays {participants[0].name} {abs(participants[-1].net)} GBP')
                # Subtract the largest loss from participant[0].net i.e. money owed
                participants[0].net -= abs(participants[-1].net)
                # Remove participants[-1] from list as they pay all to participant[0]
                participants.pop()

            # If largest win smaller than absolute largest loss
            if participants[0].net < abs(participants[-1].net):
                # The entire win is paid out by the biggest loser
                print(f'{participants[-1].name} pays {participants[0].name}'
                      f' {abs(participants[0].net)} GBP')
                # Adjusting participants[-1].net i.e. how much they still owe
                participants[-1].net += participants[0].net
                # Remove the largest winner from participants list as they have been paid fully
                participants.pop(0)

            if participants[0].net == abs(participants[-1].net):
                # Print that payout
                print(f'{participants[-1].name} pays {participants[0].name} {abs(participants[-1].net)} GBP')
                # Remove participants[-1] from list as they pay all to participant[0]
                participants.pop()
                participants.pop(0)

            # Prevents participants paying themselves zero
            if participants[0] == participants[-1]:
                break

        except IndexError:
            print('Payouts have been calculated! GG!')


Aidan = Player('Aidan', 25, 18)
Ethan = Player('Ethan', 10, 15)
Ollie = Player('Ollie', 20, 22)
Tarun = Player('Tarun', 20, 30)
Sam = Player('Sam', 30, 20)

participants = [Aidan, Ethan, Ollie, Tarun, Sam]

calculate_payouts(participants)





