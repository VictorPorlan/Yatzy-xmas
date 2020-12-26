class Yatzy:

    def __init__(self, *dices):
        self.dices = list(dices)

    @staticmethod
    def chance(*dices):
        result = 0
        for number in dices:
            result += number
        return result

    @staticmethod
    def yatzy(*dices):
        if len(set(dices)) == 1:
            return 50
        return 0


    @staticmethod
    def ones(*dices):
        amount = dices.count(1)
        return amount * 1

    @staticmethod
    def twos(*dices):
        amount = dices.count(2)
        return amount * 2
    
    @staticmethod
    def threes(*dices):
        amount = dices.count(3)
        return amount * 3

    
    def fours(self):
        amount = self.dices.count(4)
        return amount * 4
    
    
    def fives(self):
        amount = self.dices.count(5)
        return amount * 5
    
    
    def sixes(self):
        amount = self.dices.count(6)
        return amount * 6
    
    @staticmethod
    def score_pair(*dices):
        ordered_dices = sorted(dices, reverse=True)
        for number in ordered_dices:
            if ordered_dices.count(number) == 2:
                return number * 2
        return 0
    
    @staticmethod
    def two_pairs(*dices):
        ordered_dices = sorted(dices, reverse=True)
        last_number = ""
        result = 0
        pairs = 0
        for number in ordered_dices:
            if number == last_number:
                pass
            elif ordered_dices.count(number) >= 2:
                result += number * 2
                pairs += 1
            last_number = number
        if pairs == 2:    
            return result
        else:
            return 0

    
    @staticmethod
    def four_of_a_kind( *dices):
        ordered_dices = sorted(dices, reverse=True)
        for number in ordered_dices:
            if ordered_dices.count(number) >= 4:
                return number * 4
        return 0
    

    @staticmethod
    def three_of_a_kind(*dices):
        ordered_dices = sorted(dices, reverse=True)
        for number in ordered_dices:
            if ordered_dices.count(number) >= 3:
                return number * 3
        return 0
    

    @staticmethod
    def smallStraight(*dices):
        if sorted(list(dices)) == list(range(1, 6)):
            return sum(dices)
        return 0
    

    @staticmethod
    def largeStraight(*dices):
        if sorted(list(dices)) == list(range(2, 7)):
            return sum(dices)
        return 0
    

    @staticmethod
    def fullHouse(*dices):
        result = 0
        pair = False
        three_of_a_kind = False
        ordered_dices = sorted(dices, reverse=True)
        last_number = ""
        for number in ordered_dices:
            if number == last_number:
                pass
            elif ordered_dices.count(number) == 2:
                result += number * 2
                pair = True
            elif ordered_dices.count(number) == 3:
                result += number * 3
                three_of_a_kind = True
            last_number = number
        if pair == True and three_of_a_kind == True:    
            return result
        else:
            return 0
