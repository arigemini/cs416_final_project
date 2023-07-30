import csv


def main():
    names = ['SPX', 'META', 'AMZN', 'AAPL', 'NFLX', 'GOOG']

    values = {}
    for name in names:
        with open(f"{name}.csv") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                date = row['Date']
                if date not in values:
                    values[date] = {'Date': date}
                values[date][name] = row['Close']

    with open('SPX_FAANG.csv', 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=['Date'] + names)
        writer.writeheader()
        for date, info in sorted(values.items()):
            if date < '2015-01-01' or date > '2023-07-01':
                continue
            writer.writerow(info)


if __name__ == '__main__':
    main()
