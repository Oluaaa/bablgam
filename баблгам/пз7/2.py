class WeatherWarning:
    def rain(self):
        print(f"Ожидаются сильные дожди и ливни с грозой")

    def snow(self):
        print(f"Ожидается снег и усиление ветра")

    def low_temperature(self):
        print(f"Ожидается сильное понижение температуры")


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, date):
        print(f'{str(date).split('-')[0]}.{str(date).split('-')[1]}.{str(date).split('-')[2]}')
        print(f'Ожидаются сильные дожди и ливни с грозой')

    def snow(self, date):
        print(f'{str(date).split('-')[0]}.{str(date).split('-')[1]}.{str(date).split('-')[2]}')
        print(f'Ожидается снег и усиление ветра')

    def low_temperature(self, date):
        print(f'{str(date).split('-')[0]}.{str(date).split('-')[1]}.{str(date).split('-')[2]}')
        print(f'Ожидается сильное понижение температуры')


print(issubclass(WeatherWarningWithDate, WeatherWarning))

weatherwarning = WeatherWarning()

weatherwarning.rain()
weatherwarning.snow()
weatherwarning.low_temperature()

from datetime import date

weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)

