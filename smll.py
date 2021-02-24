# this is a simple experiment to create a machine learning library

"""
Copyright (C) <year>  <name of author>

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

from random import randint


# some math related functions

def generate_weight():
    return randint(0, 1000)/1000


def flatten(vector):
    out = 1
    for dimension in vector:
        out *= dimension
    return out


class Neuron:
    def __init__(self):
        self.b = generate_weight()
        self.w = generate_weight()


class InputLayer:
    def __init__(self, input_shape, activation):
        self.input_shape = input_shape
        self.neuronsNumber = flatten(self.input_shape)
        self.neurons = []

        for a in range(self.neuronsNumber):
            self.neurons.append(Neuron)


class DenseLayer:
    def __init__(self, neurons, activiation):
        self.neuronsNumber = neurons
        self.neurons = []

        for a in range(self.neuronsNumber):
            self.neurons.append(Neuron())


class Model:
    def __init__(self, layers):
        self.layers = layers
