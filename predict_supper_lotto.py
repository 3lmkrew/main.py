import pandas as pd
from collections import Counter


class PredictWinningLotto:
    """Will take in all previous supper lotto winning numbers and output most common 5 numbers and 1 most common
    mega number. Will also be able to output 5 least common numbers and 1 least mega nuber.
    """

    def __init__(self, file, sheet, num):
        self.file = file
        self.sheet = sheet
        self.num = num

    def past_winning_data_to_list(self):
        file_data = pd.read_excel(self.file, self.sheet)  # create panda object to retrieve winning number data
        list_of_rows = file_data.values.tolist()  # turn data into a list, each index is 5 winning numbers inside a list
        list_of_numbers = []  # empty list to hold all past winning numbers in single list
        for row in list_of_rows:  # iterate through main list, that has list for each set of 5 past winning numbers
            for num in row:  # iterate through each list holding 5 past winning numbers
                list_of_numbers.append(
                    num)  # append winning numbers to create 1 single list with all past winning numbers
        return list_of_numbers  # returns single list with all previous winning numbers

    def most_common_winning_nums(self):
        numbers_to_play = []
        past_winners = self.past_winning_data_to_list()
        counter = Counter(past_winners)  # pass single winning number list to Counter class
        most_common = counter.most_common(self.num)  # use .most_common() method and pass number you want to determine
        # will return a tuple (8, 6)  first number is common and second is amount of times it appears
        for number, count in most_common:  # for each tuple with the highest number
            numbers_to_play.append(number)  # append the 5 most common numbers to our first empy list
        numbers_to_play.sort()  # Sort the five most common numbers from small to large
        return numbers_to_play

    def less_common_winning_nums(self):
        less_com = []
        past_winners = self.past_winning_data_to_list()
        counter = Counter(past_winners)  # pass single winning number list to Counter class
        for each in counter:
            less_com.append(each)
        return less_com[-self.num:]


if __name__ == "__main__":
    past_winning_nums = PredictWinningLotto(file="one.xlsx", sheet="Sheet1", num=5)
    past_winning_nums.past_winning_data_to_list()
    five_common = past_winning_nums.most_common_winning_nums()
    five_less_common = past_winning_nums.less_common_winning_nums()
    print(f"The five most common supper lotto numbers are: {five_common}")
    print(f"The five least common supper lotto numbers are: {five_less_common}")

    mega_past_nums = PredictWinningLotto(file="one.xlsx", sheet="Sheet2", num=1)
    mega_past_nums.past_winning_data_to_list()
    mega_common = mega_past_nums.most_common_winning_nums()
    mega_less_common = mega_past_nums.less_common_winning_nums()
    print(f"The most common Mega: {mega_common}")
    print(f"The least common Mega: {mega_less_common}")
