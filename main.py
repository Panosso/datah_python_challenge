# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import defaultdict


def python_challenge_datah():

    class PokerHand():

        def __init__(self, hand):
            self.hand = hand

        def cards(self):
            return self.hand.split(" ")

        def compare_with(self, challenge_poker_hand):

            card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11,
                               "Q": 12, "K": 13, "A": 14}

            def check_royal_flush(hand):
                cards = ''.join([h[0] for h in hand])
                if cards == "TJQKA":
                    return True
                return False

            def check_flush(hand):
                suit = set([h[1] for h in hand])
                if len(suit) == 1:
                    return True
                else:
                    return False

            def check_straight(hand):
                card_values = [h[0] for h in hand]
                values_counts = defaultdict(lambda: 0)
                for v in card_values:
                    values_counts[v] += 1
                rank_values = [card_order_dict[i] for i in card_values]
                if rank_values == [2, 3, 4, 5, 14]:
                    rank_values = [1, 2, 3, 4, 5]
                value_range = max(rank_values) - min(rank_values)
                if len(set(values_counts.values())) == 1 and (value_range == 4):
                    return True
                else:
                    if set(values) == set(["A", "2", "3", "4", "5"]):
                        return True
                    return False

            def check_straight_flush(hand):
                if check_straight(hand) and check_flush(hand):
                    return True
                else:
                    return False

            def check_four_kind(hand):
                card_values = [i[0] for i in hand]
                value_counts = defaultdict(lambda: 0)
                for v in card_values:
                    value_counts[v] += 1
                if sorted(value_counts.values()) == [1, 4]:
                    return True
                return False

            def check_full_house(hand):
                card_values = [i[0] for i in hand]
                value_counts = defaultdict(lambda: 0)
                for v in card_values:
                    value_counts[v] += 1
                if sorted(value_counts.values()) == [2, 3]:
                    return True
                else:
                    return False

            def check_tree_kind(hand):
                card_value = [i[0] for i in hand]
                value_counts = defaultdict(lambda: 0)
                for v in card_value:
                    value_counts[v] += 1
                if set(value_counts.values()) == set([3, 1]):
                    return True
                else:
                    return False

            def check_two_pair(hand):
                card_values = [i[0] for i in hand]
                value_counts = defaultdict(lambda: 0)
                for v in card_values:
                    value_counts[v] += 1
                if sorted(value_counts.values()) == [1, 2, 2]:
                    return True
                else:
                    return False

            def check_one_pairs(hand):
                card_values = [i[0] for i in hand]
                value_counts = defaultdict(lambda: 0)
                for v in card_values:
                    value_counts[v] += 1
                if 2 in value_counts.values():
                    return True
                else:
                    return False

            def check_four_highest_card(hand):
                card_values = [h[0] for h in hand]
                value_dict = defaultdict(lambda: 0)
                for i in set(card_values):
                    value_dict[card_values.count(i)] = i

                return value_dict[4]

            def check_three_highest_card(hand):
                card_values = [h[0] for h in hand]
                value_dict = defaultdict(lambda: 0)
                for i in set(card_values):
                    value_dict[card_values.count(i)] = i

                return value_dict[3]

            def check_double_pair_highest_card(hand):
                card_values = [h[0] for h in hand]
                lista = []
                for card in card_values:
                    if card_values.count(card) == 2 and card not in lista:
                        lista.append(card)

                return card_order_dict[lista[-1]]

            def check_double_pair_highest_solo_card(hand):
                card_values = [h[0] for h in hand]
                lista = []
                for card in card_values:
                    if card_values.count(card) == 1 and card not in lista:
                        lista.append(card)

                return card_order_dict[lista[-1]]

            def check_pair_highest_solo_card(hand):
                card_values = [h[0] for h in hand]
                lista = []
                for card in card_values:
                    if card_values.count(card) == 1 and card not in lista:
                        lista.append(card)

                return card_order_dict[lista[-1]]

            def check_pair_highest_card(hand):
                card_values = [h[0] for h in hand]
                for card in card_values:
                    if card_values.count(card) == 2:
                        return card_order_dict[card]

            def get_highest_card(hand):
                value_poker_hand1 = [h[0] for h in hand]
                value_list = []
                for i in value_poker_hand1:
                    value_list.append(card_order_dict[i])
                return max(value_list)

            def get_straight_value(hand):
                card_value = [h[0] for h in hand]
                straight_sum = 0
                if card_value == ['2', '3', '4', '5', 'A']:
                    card_value = [1, 2, 3, 4, 5]
                    return sum(card_value)
                for card in card_value:
                    straight_sum += card_order_dict[card]

                return straight_sum

            values = dict(zip('23456789TJQKA', range(2, 15)))
            poker_hand_1 = sorted(self.cards(), key=lambda x: values[x[0]])
            poker_hand_2 = sorted(challenge_poker_hand.cards(), key=lambda x: values[x[0]])

            if check_royal_flush(poker_hand_1) or check_royal_flush(poker_hand_2):
                if check_royal_flush(poker_hand_1):
                    return "WIN"
                else:
                    return "LOSS"

            elif check_straight_flush(poker_hand_1) or check_straight_flush(poker_hand_2):

                if check_straight_flush(poker_hand_1) and check_straight_flush(poker_hand_2):

                    if get_highest_card(poker_hand_1) > get_highest_card(poker_hand_2):
                        return "WIN"
                    else:
                        return "LOSS"

                elif check_straight_flush(poker_hand_1):
                    return "WIN"
                else:
                    return "LOSS"

            elif check_four_kind(poker_hand_1) or check_four_kind(poker_hand_2):

                if check_four_kind(poker_hand_1) and check_four_kind(poker_hand_2):

                    if check_four_highest_card(poker_hand_1) > check_four_highest_card(poker_hand_2):
                        return "WIN"
                    else:
                        return "LOSS"

                elif check_four_kind(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            elif check_full_house(poker_hand_1) or check_full_house(poker_hand_2):

                if check_full_house(poker_hand_1) and check_full_house(poker_hand_2):

                    if check_three_highest_card(poker_hand_1) > check_three_highest_card(poker_hand_2):
                        return "WIN"
                    else:
                        return "LOSS"

                elif check_full_house(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            elif check_flush(poker_hand_1) or check_flush(poker_hand_2):

                if check_flush(poker_hand_1) and check_flush(poker_hand_2):
                    if get_highest_card(poker_hand_1) > get_highest_card(poker_hand_2):
                        return "WIN"

                    else:
                        return "LOSS"

                elif check_flush(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            elif check_straight(poker_hand_1) or check_straight(poker_hand_2):

                if check_straight(poker_hand_1) and check_straight(poker_hand_2):
                    if get_straight_value(poker_hand_1) > get_straight_value(poker_hand_2):
                        return "WIN"

                    else:
                        return "LOSS"

                elif check_straight(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            elif check_tree_kind(poker_hand_1) or check_tree_kind(poker_hand_2):

                if check_tree_kind(poker_hand_1) and check_tree_kind(poker_hand_2):

                    if check_three_highest_card(poker_hand_1) > check_three_highest_card(poker_hand_2):
                        return "WIN"

                    else:
                        return "LOSS"

                elif check_tree_kind(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            elif check_two_pair(poker_hand_1) or check_two_pair(poker_hand_2):

                if check_two_pair(poker_hand_1) and check_two_pair(poker_hand_2):

                    if check_double_pair_highest_card(poker_hand_1) > check_double_pair_highest_card(poker_hand_2):
                        return "WIN"

                    elif check_double_pair_highest_card(poker_hand_1) == check_double_pair_highest_card(poker_hand_2):

                        if check_double_pair_highest_solo_card(poker_hand_1) > check_double_pair_highest_solo_card(poker_hand_2):
                            return "WIN"

                        else:

                            return "LOSS"


                elif check_two_pair(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            elif check_one_pairs(poker_hand_1) or check_one_pairs(poker_hand_2):

                if check_one_pairs(poker_hand_1) and check_one_pairs(poker_hand_2):
                    if check_pair_highest_card(poker_hand_1) > check_pair_highest_card(poker_hand_2):
                        return "WIN"

                    elif check_pair_highest_card(poker_hand_1) == check_pair_highest_card(poker_hand_2):

                        if check_pair_highest_solo_card(poker_hand_1) > check_pair_highest_solo_card(poker_hand_2):
                            return "WIN"
                        else:

                            return "LOSS"

                    else:
                        return "LOSS"

                elif check_one_pairs(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            else:
                if get_highest_card(poker_hand_1) > get_highest_card(poker_hand_2):
                    return "WIN"

                else:
                    return "LOSS"

    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")))

    print(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JC AS KC TD")))

    print(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7C JS TS 6D")))

    print(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7S 5S 5D JS")))

    print(PokerHand("AS AD KD 7C 3D").compare_with(PokerHand("AD AH KD 7C 4S")))

    print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("AC AH AS AS KS")))

    print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JS QC KS AC")))

    print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QS QC AS 8H")))

    #No teste unitário ele está como WIN porém o resultado correto conforme as regras do poker é LOSS
    print(PokerHand("AC AH AS AS KS").compare_with(PokerHand("TC JS QC KS AC")))

    print(PokerHand("AC AH AS AS KS").compare_with(PokerHand("QH QS QC AS 8H")))

    print(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QC AS 8H")))

    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JC JS JD TH")))

    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4H 5H 9H TH JH")))

    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")))

    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))

    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))

    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H TH JH")))

    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")))

    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TH TD JH JD")))

    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("JH JD TH TC 4C")))

    print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")))

    print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))

    print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))

    print(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))

    print(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))

    print(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JH JD TH TC 4C")))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    python_challenge_datah()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
