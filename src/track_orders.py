from collections import defaultdict


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer: str, order: str, day: str) -> None:
        self.orders.append(
            {"nome": customer, "prato": order, "dia_da_semana": day}
        )

    def get_most_ordered_dish_per_customer(self, customer):
        data = self.orders
        filtred_data = [order for order in data if order["nome"] == customer]
        plate_counts = {}
        for order in filtred_data:
            plate = order["prato"]
            if plate in plate_counts:
                plate_counts[plate] += 1
            else:
                plate_counts[plate] = 1
        return max(plate_counts, key=plate_counts.get)

    def get_never_ordered_per_customer(self, customer):
        data = self.orders
        customer_orders = [item for item in data if item['nome'] == customer]
        customer_plates = [item['prato'] for item in customer_orders]
        all_plates = set([item['prato'] for item in data])

        never_ordered_plates = all_plates - set(customer_plates)

        return never_ordered_plates

    def get_days_never_visited_per_customer(self, customer):
        data = self.orders
        customer_orders = [item for item in data if item['nome'] == customer]
        customer_days = [item['dia_da_semana'] for item in customer_orders]
        all_days = set([item['dia_da_semana'] for item in data])

        never_ordered_days = all_days - set(customer_days)

        return never_ordered_days

    def get_busiest_day(self):
        data = self.orders
        days_count = defaultdict(int)
        for entry in data:
            days_count[entry['dia_da_semana']] += 1
        return max(days_count, key=days_count.get)

    def get_least_busy_day(self):
        data = self.orders
        days_count = defaultdict(int)
        for entry in data:
            days_count[entry['dia_da_semana']] += 1
        return min(days_count, key=days_count.get)
