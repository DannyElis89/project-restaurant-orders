import os
import csv
from statistics import mode


def analyze_log(path_to_file):
    filename, extensao = os.path.splitext(path_to_file)

    if extensao != '.csv':
        raise FileNotFoundError(
            f"Extensão inválida: '{filename}{extensao}'"
            )

    try:
        with open(path_to_file) as file:
            orders = list(csv.reader(file))
            # print('+++++++++++++++')
            # print(orders)

            maria_favorite_food = mode([
              (order[1])
              for order in orders
              if order[0] == 'maria'
            ])
            # print(maria_favorite_food)

            arnaldos_hamburguers = [
                order[1]
                for order in orders
                if order[0] == 'arnaldo' and order[1] == 'hamburguer'
            ]
            len_arnaldos_hamburguers = len(arnaldos_hamburguers)
            # print(arnaldos_hamburguers)
            # print(len_arnaldos_hamburguers)

            all_foods = [order[1] for order in orders]
            # print(all_foods)
            set_all_foods = set(all_foods)
            # print(set_all_foods)

            joao_never_ordered = set_all_foods.difference(set([
                order[1]
                for order in orders
                if order[0] == 'joao'
            ]))

            working_days = [order[2] for order in orders]
            # print(working_days)
            set_working_days = set(working_days)

            set_days_joao = set([
                order[2]
                for order in orders
                if order[0] == 'joao'
            ])
            days_joao_never_showup = set_working_days.difference(set_days_joao)
            # print(set_days_joao)
            # print(days_joao_never_showup)

            lines = [
                maria_favorite_food,
                len_arnaldos_hamburguers,
                joao_never_ordered,
                days_joao_never_showup
                ]

            with open('data/mkt_campaign.txt', "w") as txt:
                for line in lines:
                    txt.write(f'{line}\n')

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{filename}{extensao}'")
