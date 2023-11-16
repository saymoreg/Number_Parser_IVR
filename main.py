data = {}


import json

international_numbers = {}


def find_international_numbers(conditions, phone):
    for case in ('#or', '#and'):
        if case in conditions:
            for or_and_cond in conditions[case]:
                find_international_numbers(or_and_cond, phone)
    if "line" in conditions:
        lines = conditions["line"]["#in"]
        for line in lines:
            if "intl" in line and ("logistic" not in line and "logictic" not in line):
                if international_numbers.get(phone):
                    if line not in international_numbers[phone]:
                        international_numbers[phone].append(line)
                else:
                    international_numbers[phone] = [line]


# Поиск международных номеров и связанных линий
for source in data['sources']:
    find_international_numbers(source["conditions"], source['phone'])

# Вывод результатов
for phone_number, lines in international_numbers.items():
    lines_str = ', '.join(lines)
    print(f"Номер: {phone_number} -- Линии: {lines_str}")
