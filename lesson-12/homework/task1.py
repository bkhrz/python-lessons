from bs4 import BeautifulSoup
import statistics

with open('weather.html', 'r', encoding = 'utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

weather_data = []
table_rows = soup.find('tbody').find_all('tr')

# extract data
for row in table_rows:
    cols = row.find_all('td')
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace('°C', ''))
    cond = cols[2].text.strip()
    weather_data.append((day, temp, cond))

# prints weather forecast
for day, temp, cond in weather_data:
    print(f'{day}, {temp}C, {cond}')

if weather_data:

    max_temp = max(weather_data, key=lambda x: x[1])[1]
    hottest_days = [day for day, temp, cond in weather_data if temp == max_temp]
    print(f"\nHottest Day(s): {', '.join(hottest_days)} with {max_temp}°C")

    sunniest_day = [day for day, temp, cond in weather_data if cond == 'Sunny']
    print(f"The sunniest day(s): {','.join(sunniest_day)}")

    avrg_temp = statistics.mean([temp for day, temp, cond in weather_data])
    print(f'Average temp: {avrg_temp}C')

