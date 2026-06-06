from utils.query2_namedTuples import *
from typing import Tuple

# Questa funzione converte una stringa in un float. Se la stringa è "None" ritorna il tipo None, che è un singletone Python e occupa meno memoria
def to_float(string):
    return float(string) if string != "None" else None

# Questa funzione effettua il parsing delle stringhe lette dal file csv e ritorna una coppia chiave-valore del tipo (carrier, (arr_del, cancelled, diverted, carrier_delay,
# weather_delay, nas_delay, security_delay, late_aircraft_delay))
def parse_line(line):

    # Indici:
    #   - OP_UNIQUE_CARRIER 1
    #   - ARR_DELAY 3
    #   - CANCELLED 4
    #   - DIVERTED 5
    #   - CARRIER_DELAY 6
    #   - WEATHER_DELAY 7
    #   - NAS_DELAY 8
    #   - SECURITY_DELAY 9
    #   - LATE_AIRCRAFT_DELAY 10

    line = line.split(",")

    key = line[1]
    value = BaseRecord(to_float(line[3]), to_float(line[4]), to_float(line[5]), to_float(line[6]),
                       to_float(line[7]), to_float(line[8]), to_float(line[9]), to_float(line[10]))

    return key, value

def func_in(acc, value:BaseRecord):
    sum_not_canc_div = acc[0] + 1 if not (value.cancelled or value.diverted) else acc[0]
    sum_arr_delay = acc[1][0]  if value.arr_delay is None else acc[1][0] + value.arr_delay
    count_arr_delay = acc[1][1]  if value.arr_delay is None else acc[1][1] + 1
    sum_carrier_delay = acc[2][0] if value.carrier_delay is None else acc[2][0] + value.carrier_delay
    count_carrier_delay = acc[2][1] if value.carrier_delay is None else acc[2][1] + 1
    sum_nas_delay = acc[3][0] if value.nas_delay is None else acc[3][0] + value.nas_delay
    count_nas_delay = acc[3][1] if value.nas_delay is None else acc[3][1] + 1
    sum_security_delay = acc[4][0] if value.security_delay is None else acc[4][0] + value.security_delay
    count_security_delay = acc[4][1] if value.security_delay is None else acc[4][1] + 1
    sum_weather_delay = acc[5][0] if value.weather_delay is None else acc[5][0] + value.weather_delay
    count_weather_delay = acc[5][1] if value.weather_delay is None else acc[5][1] + 1
    sum_aircraft_delay = acc[6][0] if value.late_aircraft_delay is None else acc[6][0] + value.late_aircraft_delay
    count_aircraft_delay = acc[6][1] if value.late_aircraft_delay is None else acc[6][1] + 1

    return (sum_not_canc_div, (sum_arr_delay, count_arr_delay), (sum_carrier_delay, count_carrier_delay), (sum_nas_delay, count_nas_delay),
            (sum_security_delay, count_security_delay), (sum_weather_delay, count_weather_delay), (sum_aircraft_delay, count_aircraft_delay))


def func_between(acc1, acc2):
    total_not_canc_div = acc1[0] + acc2[0]
    arr_delay_total = acc1[1][0] + acc2[1][0]
    arr_delay_count = acc1[1][1] + acc2[1][1]
    carrier_delay_total = acc1[2][0] + acc2[2][0]
    carrier_delay_count = acc1[2][1] + acc2[2][1]
    nas_delay_total = acc1[3][0] + acc2[3][0]
    nas_delay_count = acc1[3][1] + acc2[3][1]
    security_delay_total = acc1[4][0] + acc2[4][0]
    security_delay_count = acc1[4][1] + acc2[4][1]
    weather_delay_total = acc1[5][0] + acc2[5][0]
    weather_delay_count = acc1[5][1] + acc2[5][1]
    late_aircraft_delay_total = acc1[6][0] + acc2[6][0]
    late_aircraft_delay_count = acc1[6][1] + acc2[6][1]

    return (total_not_canc_div, (arr_delay_total, arr_delay_count), (carrier_delay_total, carrier_delay_count), (nas_delay_total, nas_delay_count),
            (security_delay_total, security_delay_count), (weather_delay_total, weather_delay_count), (late_aircraft_delay_total, late_aircraft_delay_count))


def compute_avgs(record):
    value = record[1]

    total_not_canc_div = value[0]
    arr_del_avg = value[1][0] / value[1][1]
    carrier_del_avg = value[2][0] / value[2][1]
    nas_delay_avg = value[3][0] / value[3][1]
    security_delay_avg = value[4][0] / value[4][1]
    weather_del_avg = value[5][0] / value[5][1]
    late_aircraft_delay_avg = value[6][0] / value[6][1]

    return record[0], (total_not_canc_div, arr_del_avg, carrier_del_avg, nas_delay_avg, security_delay_avg, weather_del_avg, late_aircraft_delay_avg)

def format_data(record):

    return f"{record[0]},{record[1][0]},{record[1][1]:.2f},{record[1][2]:.2f},{record[1][5]:.2f},{record[1][3]:.2f},{record[1][4]:.2f},{record[1][6]:.2f}"
