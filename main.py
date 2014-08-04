#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        search_tpl = "http://api.openweathermap.org/data/2.5/find?q={0}&type=like"
        search_url = search_tpl.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        cities = ["{0}({1})".format(d['name'], d['sys'], ['country']) for d in data['list']]
        self.search_result.item_strings = cities


class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()
