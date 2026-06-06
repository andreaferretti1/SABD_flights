def parse_and_map_line(line: str):

    # Indici
    #   - MONTH 1
    #   - OP_UNIQUE_CARRIER 2
    #   - DEP_DELAY 13
    #   - ARR_DELAY 16
    #   - CANCELLED 17
    #   - DIVERTED 19
    #   - CARRIER_DELAY 22
    #   - WEATHER_DELAY 23
    #   - NAS_DELAY
    #   - SECURITY_DELAY
    #   -LATE_AIRCRAFT_DELAY

    cols_to_save = {1, 3, 13, 16, 17, 19, 22, 23, 24, 25, 26}

    fields = line.split(",")

    processed_fields = ["None" if value == "" else value for pos, value in enumerate(fields) if pos in cols_to_save]

    return ",".join(processed_fields)


