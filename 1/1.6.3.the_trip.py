import decimal
import fileinput


def normalize_expenses(costs):
    mean = decimal.Decimal(sum(costs) / len(costs))
    # Truncate fractional cents
    mean = mean.quantize(decimal.Decimal('1.00'), rounding=decimal.ROUND_DOWN)
    mean = float(mean)
    balance = sum(mean - c for c in costs if c < mean)
    return balance


if __name__ == '__main__':
    lines = fileinput.input()
    for line in lines:
        n = int(line)
        costs = [float(next(lines)) for student in range(n)]
        if costs:
            balance = normalize_expenses(costs)
            print('${:.2f}'.format(balance))
