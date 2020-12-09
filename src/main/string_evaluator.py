# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World" # TODO - Implement solution

    def concatenate(self, value_to_be_added_to, value_to_add):
        return str(value_to_be_added_to) + str(value_to_add) # TODO - Implement solution

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        return str(string_to_fetch_from)[starting_index:(ending_index+1)] # TODO - Implement solution

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        return str(string_to_fetch_from)[(starting_index+1):ending_index] # TODO - Implement solution

    def compare(self, first_value, second_value):
        # switch - case statements
        if str(first_value) in ("None", "False"):
            first_value = 0
        elif str(first_value) == ("True"):
            first_value = 1
        elif str(second_value) in ("None", "False"):
            second_value = 0
        elif str(second_value) == ("True"):
            second_value = 1

        comparison = (str(first_value) == str(second_value))
        return comparison     # TODO - Implement solution

    def get_middle_character(self, string_to_fetch_from):
        is_even = (len(string_to_fetch_from) % 2) == 0
        if is_even:
            return "String to fetch middle character from is an even number"
        else:
            return string_to_fetch_from[len(string_to_fetch_from) / 2]  # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        return string_to_fetch_from.split()[0] # TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
        return string_to_fetch_from.split()[1] # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1] # TODO - Implement solution