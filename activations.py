# in this file there are all of the activation functions

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

import math

def sigmoid(input_value):
    out = []
    
    for value in input_value:
        out.append(1/(1+math.exp(-value)))
    
    return out


def relu(input_value):
    out = []
    
    for value in input_value:
        out.append(max(0, value))
    
    return out


def softmax(input_value):
    out = []

    expo_sum = 0
    for value in input_value:
        expo_sum += math.exp(value)
    
    for value in input_value:
        out.append(math.exp(value) / expo_sum)
    
    return out
