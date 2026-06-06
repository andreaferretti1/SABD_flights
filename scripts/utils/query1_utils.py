# Questa funzione converte una stringa in un float. Se la stringa è "None" ritorna il tipo None, che è un singletone Python e occupa meno memoria
def to_float(string):
    return float(string) if string != "None" else None


# Questa funzione effettua il parsing delle stringhe lette da csv, e converte i campi nel formato opportuno
def parse_line(line):

    # Indici:
    #    - MONTH 0
    #    - OP_UNIQUE_CARRIER 1
    #    - DEP_DELAY 2
    #    - CANCELLED 4

    line = line.split(",")

    return (line[1], int(line[0])), (to_float(line[2]), to_float(line[4]))


def func_in(acc, value):
    sum_dep_delay = acc[0][0] if value[1] == 1 or value[0] is None else acc[0][0] + value[0]
    count_dep_delay = acc[0][1] if value[1] == 1 or value[0] is None else acc[0][1] + 1
    max_dep_delay = acc[1] if value[1] == 1 or value[0] is None else max(acc[1], value[0])
    min_dep_delay = acc[2] if value[1] == 1 or value[0] is None else min(acc[2], value[0])
    sum_canc = acc[3][0] + value[1]
    count_canc = acc[3][1] + 1

    return (sum_dep_delay, count_dep_delay), max_dep_delay, min_dep_delay, (sum_canc, count_canc)


def func_between(acc1, acc2):
    sum_dep_delay = acc1[0][0] + acc2[0][0]
    count_dep_delay = acc1[0][1] + acc2[0][1]
    max_dep_delay = max(acc1[1], acc2[1])
    min_dep_delay = min(acc1[2], acc2[2])
    sum_canc = acc1[3][0] + acc2[3][0]
    count_canc = acc1[3][1] + acc2[3][1]

    return (sum_dep_delay, count_dep_delay), max_dep_delay, min_dep_delay, (sum_canc, count_canc)


def compute_frac(record):
    value = record[1]

    avg_dep_delay = value[0][0] / value[0][1] if value[0][1] > 0 else 0
    canc_rate = value[3][0] / value[3][1] if value[3][1] > 0 else 0

    return record[0], (avg_dep_delay, value[1], value[2], canc_rate)


# Questa funzione formatta ciascun elemento dell'rdd contenente i risultati
def format_data(element):
    key = element[0]
    value = element[1]

    month = key[1]
    airline_company = key[0]
    del_mean = value[0]
    del_min = value[2]
    del_max = value[1]
    canc_rate = value[3]


    return f"{month},{airline_company},{del_mean:.2f},{del_min:.2f},{del_max:.2f},{canc_rate:.2f}"
