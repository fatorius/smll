# in this file there are all of the model classes

"""
Copyright (C) 2021 HugoSouza

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# email: contato@hugosouza.com


class Sequential:
    def __init__(self, layers):
        self.layers = layers

    def add(self, new_layer):
        self.layers.append(new_layer)

    def run(self, value):
        current_value = value
        for layer in self.layers:
            current_value = layer.feedfoward(current_value)

        return current_value

