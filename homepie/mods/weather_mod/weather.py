import requests
import re
from parsel import Selector


url = "https://www.wetteronline.de/wetter/karlsruhe"
html = requests.get(url).text
selector = Selector(text=html)


def current_temperature():
    path_current = """//div[@id="totalcontainer"]/div[@id="leftcontainer"]/div[@id="contentcontainer"]/
                  div[@id="content"]/div[@id="maincontent"]
                  /div[@id="pc"]/div[@id="product"]/div[@id="p_city_weather"]
                  /div[@id="product_display"]/div[1]/div[@class="forecast visible"]/div[@id="nowcast-card-temperature"]
                  /div[@class="value"]/text()"""
    currently = selector.xpath(path_current).get()

    return currently


def hourly_temperature():
    path_hourly = """//div[@id="totalcontainer"]/div[@id="leftcontainer"]/div[@id="contentcontainer"]/
                      div[@id="content"]/div[@id="maincontent"]
                      /div[@id="pc"]/div[@id="product"]/div[@id="p_city_weather"]
                      /div[@id="product_display"]/div[1]/div[@class="forecast visible"]/div[@class="forecast-container"]
                      /div[@class="faded-background-container"]/div[@id="hourly-container"]/script/text()"""

    hourly = selector.xpath(path_hourly)

    list = []
    time = ""
    hour = ""
    for index, hour in enumerate(hourly):
        hourly_a = hour.get().split("\n")
        counter = 0
        for hour_text in hourly_a:
            if counter < len(hourly_a) - 1:
                if "hour:" in hour_text:
                    time = re.sub("\D+", "", hour_text)
                if "temperature:" in hour_text:
                    hour = re.sub("\D+", "", hour_text)
                counter += 1
            else:
                list.append((time, hour))

    return list


def tomorrows_temperature():
    path_tomorrow = """//div[@id="totalcontainer"]/div[@id="leftcontainer"]/div[@id="contentcontainer"]/
                      div[@id="content"]/div[@id="maincontent"]
                      /div[@id="pc"]/div[@id="product"]/div[@id="p_city_weather"]
                      /div[@id="product_display"]/div[1]/div[@class="forecast visible"]/div[@class="forecast-container"]
                      /div[@class="faded-background-container"]/div[@id="weatherreport-catchline"]
                      /div[@data-day="tomorrow"]/text()"""

    tomorrow = selector.xpath(path_tomorrow)

    print(tomorrow.get())
    return re.sub("\D+", "", tomorrow.get())


def today_forecast():
    path_today = """//div[@id="totalcontainer"]/div[@id="leftcontainer"]/div[@id="contentcontainer"]/
                          div[@id="content"]/div[@id="maincontent"]
                          /div[@id="pc"]/div[@id="product"]/div[@id="p_city_weather"]
                          /div[@id="product_display"]/div[1]/div[@class="forecast visible"]/div[@class="forecast-container"]
                          /div[@class="faded-background-container"]/div[@id="weatherreport-catchline"]
                          /div[@data-day="today"]/text()"""

    today = selector.xpath(path_today)

    return "%s%s Grad." % (today.get(), current_temperature())


def tomorrows_forecast():
    path_tomorrow = """//div[@id="totalcontainer"]/div[@id="leftcontainer"]/div[@id="contentcontainer"]/
                          div[@id="content"]/div[@id="maincontent"]
                          /div[@id="pc"]/div[@id="product"]/div[@id="p_city_weather"]
                          /div[@id="product_display"]/div[1]/div[@class="forecast visible"]/div[@class="forecast-container"]
                          /div[@class="faded-background-container"]/div[@id="weatherreport-catchline"]
                          /div[@data-day="tomorrow"]/text()"""

    tomorrow = selector.xpath(path_tomorrow)

    return tomorrow.get()


# currently not working
def current_weather_state():
    path_current = """//div[@id="totalcontainer"]/div[@id="leftcontainer"]/div[@id="contentcontainer"]/
                  div[@id="content"]/div[@id="maincontent"]
                  /div[@id="pc"]/div[@id="product"]/div[@id="p_city_weather"]
                  /div[@id="product_display"]/div[1]/div[@id="nowcast-bar-wrapper"]/div[@id="nowcast-content"]
                  /p[@id="nowcast-second-line"]"""
    currently = selector.xpath(path_current).get()

    return currently
