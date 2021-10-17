def get_parameters_from_file(filename='Parameters'):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.replace('\n', "") for line in lines if len(line) > 1]
    key = None
    anomaly_dict = {}
    for line in lines:
        if line[0] == "#":
            key = line[1:].lower()
            anomaly_dict[key] = {}
        else:
            words = line.split()
            subkey = words[0].lower()
            value = words[1]
            try:
                value = int(value)
            except:
                try:
                    value = float(value)
                except:
                    pass

            anomaly_dict[key][subkey] = value

    return anomaly_dict
