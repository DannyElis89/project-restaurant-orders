from statistics import mode
from collections import Counter


class TrackOrders:
    def __init__(self):
        self.__orders = list()

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.__orders)

    def add_new_order(self, customer, order, day):
        self.__orders.append([customer, order, day])
        return self.__len__()

    def get_most_ordered_dish_per_customer(self, customer):
        most_ordered_dish = mode(
            [order[1] for order in self.__orders
             if order[0] == customer]
        )
        return most_ordered_dish

    def get_never_ordered_per_customer(self, customer):
        set_orders = set([order[1] for order in self.__orders])
        set_difference = set_orders.difference(set(
            [order[1] for order in self.__orders if order[0] == customer]
        ))
        return set_difference

    def get_days_never_visited_per_customer(self, customer):
        set_days = set([order[2] for order in self.__orders])
        set_difference = set_days.difference(set(
            [order[2] for order in self.__orders if order[0] == customer]
        ))
        return set_difference

    def get_busiest_day(self):
        busiest_day = mode([order[2] for order in self.__orders])
        return busiest_day

    def get_least_busy_day(self):
        counter = Counter([order[2] for order in self.__orders])
        list_enumerate = list(enumerate(counter))[-1][1]
        return list_enumerate
