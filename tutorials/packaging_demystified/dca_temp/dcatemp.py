"""
Print current weather at Washington National Airport.
"""
#!/usr/bin/env python
import requests
import bs4

__version__ = "1.0.0"

def print_weather():
    def send_request():
        url = "https://forecast.weather.gov/MapClick.php?lat=38.932480000000055&lon=-77.02942999999993"
        res = requests.get(url)
        try:
            res.raise_for_status()
        except Exception as exc:
            print(f'There was a prolem: {exc}')
        return res

    def parse_html(res):
        # bs4 parses (analyze and identify parts of) an HTML file.
        bs = bs4.BeautifulSoup(res.text, 'html.parser')
        # Get detailed forecast for today and tomorrow.
        detail_forecast_period = bs.select("div #detailed-forecast-body b")
        detail_forecast_text = bs.select("div #detailed-forecast-body div .forecast-text")
        temperature_match = bs.select("div #current_conditions-summary")
        return detail_forecast_period, detail_forecast_text, temperature_match

    def weather(forecast):
        """Print current weather."""
        detail_forecast_period, detail_forecast_text, temperature_match = forecast
        weather = "\nCurrent weather summary\nWashington National Airport\n"
        weather += temperature_match[0].getText().strip() + '\n'
        for _ in range(3):
            weather += detail_forecast_period[_].getText() + ' -- ' + detail_forecast_text[_].getText() + '\n'
        weather += 'Have a lovely day ~'
        return weather

    res = send_request()
    forecast = parse_html(res)
    print(weather(forecast))

if __name__ == "__main__":
    print_weather()