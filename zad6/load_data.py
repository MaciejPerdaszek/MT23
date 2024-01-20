from zad6.data_structure import Customer


def __remove_additional_spaces(string: str) -> str:
    return ' '.join(string.split())


def __get_customers_data(file_name: str) -> []:
    data = []
    with open('./data/' + file_name, 'r') as f:
        for line in f:
            line = __remove_additional_spaces(line.strip())
            data.append(line)
    return data


def get_vehicle_data() -> []:
    data = {}
    with open('./data/vehicle-capacity.txt', 'r') as f:
        for line in f:
            line.strip()
            elements = line.split(' ')
            data[elements[0]] = int(elements[1])
    return data


def get_customers_from_file(file_name: str) -> [Customer]:
    data = __get_customers_data(file_name)
    customers = []
    for line in data:
        line = line.split(' ')
        customers.append(Customer(
            int(line[0]),
            float(line[1]),
            float(line[2]),
            float(line[3]),
            float(line[4]),
            float(line[5]),
            float(line[6])
        ))
    return customers
