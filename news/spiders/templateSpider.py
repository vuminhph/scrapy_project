import scrapy
import codecs
from unidecode import unidecode


class TemplateSpider(scrapy.Spider):
    name = 'templateSpider'
    start_urls = ['http://timbus.vn/fleets.aspx']

    def parse(self, response):

        buses = {}

        for index, bus in enumerate(response.xpath('//td[@class = "m-fleet-title txtRoute-search"]/text()').getall(), 1):
            pv1 = bus.find('[')
            pv2 = bus[pv1:].find(']') + pv1 + 1
            bus = bus[pv1:pv2]
            buses.update({str(index): bus})

        for index, Stop in enumerate(response.xpath('//td[@class = "m-fleet-item-content txtRoad-go-search"]/text()').getall(), 1):
            bus = {buses.pop(str(index)): Stop.replace(
                ' - ', '|').replace(' – ', '|') + '*'}
            buses.update(bus)

        bus_export = str(buses).replace(
            "'", '').replace('"', '').replace('*, ', '\n').replace(', ', ',').replace('.', '')
        number_of_lines = len(bus_export.split("\n"))
        bus_export = str(number_of_lines) + bus_export
        bus_export = bus_export.replace(': ', '\n')
        bus_export = unidecode(bus_export)

        print(bus_export)

        f = open("busStop.txt", "w+")
        f.write(bus_export)
        f.close()
