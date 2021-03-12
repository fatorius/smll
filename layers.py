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
import activations as activations


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
        # todo exceptions handle
        pass


class Neuron:
    def __init__(self, shape):
        self.b = []
        self.w = []

        for a in range(flatten(shape)):
            self.b.append(generate_weight())
            self.w.append(generate_weight())

    def weight(self, values):
        for pos, value in enumerate(values):
            values[pos] = (value * self.w[pos]) + self.b[pos]

        return values


class Dense:
    def __init__(self, neurons, input_shape, activation):
        self.input_shape = input_shape
        self.neurons_number = neurons
        self.neurons = []
        self.activation = get_activation_function(activation)
        self.value = []

        for a in range(self.neurons_number):
            self.neurons.append(Neuron(self.input_shape))

    def feedfoward(self, input_data):
        # TODO test if input shape is valid
        out = []
        for neuron in self.neurons:
            out.append(sum(neuron.weight(input_data)))
        self.value = self.activation(out)

        return self.value
