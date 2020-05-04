class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        self.new_card_num = ""
        self.card_num = self.card_num.replace(" ", "")
        if not self.card_num or not self.card_num.isdigit() or len(self.card_num) <=1:
            return False
        num_list = list(self.card_num)
        for i in range(-2, -len(num_list)-1, -2):
            nn = int(num_list[i])*2
            if nn>9:
                nn -= 9
                num_list[i] = str(nn)
            else:
                num_list[i] = str(nn)
        self.new_card_num = "".join(num_list)
        answer = sum(map(int, list(self.new_card_num)))
        if answer%10==0:
            return True
        else:
            return False
    
n = Luhn("055 444 285")
print(n.valid())
print(n.valid())