# Author: Mason Hernandez
# Date: 11/4/2022
# Description: Will loop through all pass winning numbers and select 5 most comment numbers and 1 mega number.
# Share winnings if you win ;)


from predict_supper_lotto import PredictWinningLotto

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

