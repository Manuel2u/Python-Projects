def invest(amount,rate,years):
    interest = (amount*rate*years/100 + amount)
    for num_years in range(1,5):
        print(f"year {num_years} : ${interest:.2f}")
        interest = interest*rate*years/100 + interest

amount = float(input('Amount = '))
rate = int(input ("rate = "))
years = int(input('years = '))   

invest(amount,rate,years)
