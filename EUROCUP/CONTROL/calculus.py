



class Calculations:
    amount_to_bet = 10
    

    @property
    def value_generators(self):
        x = 0
        for i in range(self.amount_to_bet*100):
            x += 0.01
            y = self.amount_to_bet - x
            my_tuple = (round(x, 2), round(y, 2))
            yield my_tuple
    

    def betFOO_calculations(self, first_value, second_value, mess, quantity):

        for my_tuple in self.value_generators:
            
            if (my_tuple[0]*first_value > self.amount_to_bet) and \
            (my_tuple[1]*second_value > self.amount_to_bet):
                profit_1 = (my_tuple[0]*first_value) - self.amount_to_bet
                profit_2 = (my_tuple[1]*second_value) - self.amount_to_bet
                my_sust = round((profit_2 - profit_1), 3)
                
                if -0.035 <= my_sust <= 0.035:
                    real_value = quantity / 10
                    return f"Bet {my_tuple[0]*real_value} to {first_value} and your profit will be {round(profit_1, 2)}\
                            \nBet {my_tuple[1]*real_value} to {second_value} and your profit will be {round(profit_2, 2)}\
                            \nNota: {mess}"


