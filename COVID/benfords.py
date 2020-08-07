import pandas as pd
import math
import matplotlib.pyplot as plt

def benfordNumber(benfordTest):
    sum = 0;
    for val1,val2 in zip(benfordTest,benford):
        sum += abs(val1-val2)
    return sum

benford = [math.log10(1+1/value)*100 for value in range(1,10)]
digits = [value for value in range(1,10)]

data = pd.read_csv("covid_19_data.csv")
CountryList = data['Country/Region'].unique()

# confirmed = data['Confirmed'].to_numpy()
benCountries = []
bennums = []
bencounts = []
for Country in CountryList:
    confirmed = data.loc[data['Country/Region'] == Country]['Confirmed'].to_numpy()

    freq = [0 for value in range(1,10)]
    count = 0
    for val in confirmed:
        if val != 0:
            digitCount = int(math.log10(val))
            lead = int((val / pow(10, digitCount)))
            freq[lead-1] += 1
            count += 1
    benfordTest = ([(val / count) * 100 for val in freq])
    if count > 1000:
        benCountries.append(Country)
        bennums.append(benfordNumber(benfordTest))
        bencounts.append(count)

newdata = {
    'Country': benCountries,
    'Error': bennums,
    'Sample Size': bencounts
}
newdata = pd.DataFrame(newdata)

newdata = newdata.sort_values(by=['Error'])
print(newdata)

# # Ploting
# plt.plot(digits, benford, label = 'Benford Numbers')
# plt.plot(digits, benfordTest, label = 'US Numbers')
# plt.title('Benford Test')
# plt.ylabel('Frequency of leading digits')
# plt.xlabel('Digits')
# plt.legend(loc="upper right")
# plt.show()

newdata.to_csv('temp.csv')
