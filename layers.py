# in this file there are all of the layer classes

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

from random import randint
import smll.activations as activations


def generate_weight():
    return randint(0, 1000)/1000


def flatten(vector):
    out = 1
    for dimension in vector:
        out *= dimension

    if out == 0:
        raise Exception("input shape inválida, um dos eixos está nulo.")
    return out


def get_activation_function(activation):
        if activation == "relu":
            return activations.relu
        elif activation == "sigmoid":
            return activations.sigmoid
        elif activation == "softmax":
            return activations.softmax
        else:
            # exceptions handle 
            pass


class Neuron:
    def __init__(self, shape, activation):
        self.b = []
        self.w = []

        for a in range(flatten(shape)):
            self.b.append(generate_weight())
            self.w.append(generate_weight())

        self.activate = get_activation_function(activation)

    def weight(self, values):
        for pos, value in enumerate(values):
            value = (value * self.w[pos]) + self.b[pos]

        return self.activate(values)


class DenseLayer:
    def __init__(self, neurons, input_shape, activation):
        self.input_shape = input_shape
        self.neurons_number = neurons
        self.neurons = []
        self.activation = activation
        self.value = []

        for a in range(self.neurons_number):
            self.neurons.append(Neuron(self.input_shape, self.activation))

    def feedfoward(self, input_data):
        #TODO test if input shape is valid
        out = []
        for neuron in self.neurons:
            out.append(sum(neuron.weight(input_data)))
        self.value = out

    def output(self, input_data):
        #TODO test if input shape is valid
        out = []
        for neuron in self.neurons:
            out.append(neuron.weight(input_data))
        self.value = out
            