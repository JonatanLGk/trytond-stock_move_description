# This file is part stock_move_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['PurchaseLine']


class PurchaseLine:
    __metaclass__ = PoolMeta
    __name__ = 'purchase.line'

    def get_move(self):
        # copy description from sale to shipment
        move = super(PurchaseLine, self).get_move()

        if move:
            move.description = self.description

        return move
