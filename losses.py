# in this file there are all of the loss functions

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


def mae(x, y):
    loss = []

    for pos, value in enumerate(x):
        loss.append(abs(y[pos] - value))

    return sum(loss) / len(loss)


def mse(x, y):
    loss = []

    for pos, value in enumerate(x):
        loss.append(abs(y[pos] ** 2 - value ** 2))

    return sum(loss) / len(loss)
