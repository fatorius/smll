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

import losses as losses


def get_loss_functions(loss):
    if loss == "mae":
        return losses.mae
    elif loss == "mse":
        return losses.mse
    else:
        # TODO invalid loss function
        pass


class Sequential:
    def __init__(self, layers):
        self.layers = layers
        self.learning_rate = 0
        self.loss = "none"
        self.layers_num = len(self.layers)

    def add(self, new_layer):
        self.layers.append(new_layer)
        self.layers_num = len(self.layers)

    def run(self, value):
        current_value = value
        for layer in self.layers:
            current_value = layer.feedfoward(current_value)

        return current_value

    def compile(self, learning_rate, loss):
        # TODO check if the loss and learning rate are valids
        self.learning_rate = learning_rate
        self.loss = get_loss_functions(loss)

    def evaluate(self, x, y):
        return self.loss(self.run(x), y)

    def backpropagate(self, in_value, out_expected):
        orig_loss = self.loss(self.run(in_value), out_expected)

        for layer in range(self.layers_num):
            for neuron in range(self.layers[layer].neurons_num):
                for weight in range(self.layers[layer].neurons[neuron].w_num):

                    # weight
                    original_w = self.layers[layer].neurons[neuron].w[weight]

                    # increase
                    self.layers[layer].neurons[neuron].w[weight] += self.learning_rate
                    new_loss = self.loss(self.run(in_value), out_expected)
                    if new_loss < orig_loss:
                        original_w += self.learning_rate
                        continue
                    else:
                        self.layers[layer].neurons[neuron].w[weight] = original_w

                    # decrase
                    self.layers[layer].neurons[neuron].w[weight] -= self.learning_rate
                    new_loss = self.loss(self.run(in_value), out_expected)
                    if new_loss < orig_loss:
                        original_w -= self.learning_rate
                        continue
                    else:
                        self.layers[layer].neurons[neuron].w[weight] = original_w

                # bias
                original_b = self.layers[layer].neurons[neuron].w[weight]

                # increase
                self.layers[layer].neurons[neuron].b[weight] += self.learning_rate
                new_loss = self.loss(self.run(in_value), out_expected)
                if new_loss < orig_loss:
                    original_b += self.learning_rate
                    continue
                else:
                    self.layers[layer].neurons[neuron].b[weight] = original_b

                # decrase
                self.layers[layer].neurons[neuron].b[weight] -= self.learning_rate
                new_loss = self.loss(self.run(in_value), out_expected)
                if new_loss < orig_loss:
                    original_b -= self.learning_rate
                    continue
                else:
                    self.layers[layer].neurons[neuron].w[weight] = original_b

    def train(self, set_x, set_y, epochs):
        for epoch in range(epochs):
            # print("Epoch: " + str(epoch))
            for pos, x in enumerate(set_x):
                self.backpropagate(set_x[pos], set_y[pos])
