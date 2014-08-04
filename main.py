#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        print("Explicit is better than implicit.")

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()
