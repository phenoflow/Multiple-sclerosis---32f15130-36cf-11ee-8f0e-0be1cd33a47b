# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"F20..00","system":"readv2"},{"code":"20493.0","system":"med"},{"code":"23730.0","system":"med"},{"code":"3440.0","system":"med"},{"code":"40344.0","system":"med"},{"code":"684.0","system":"med"},{"code":"69886.0","system":"med"},{"code":"95972.0","system":"med"},{"code":"96246.0","system":"med"},{"code":"96291.0","system":"med"},{"code":"96607.0","system":"med"},{"code":"97487.0","system":"med"},{"code":"98835.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('multiple-sclerosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["sclerosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["sclerosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["sclerosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
