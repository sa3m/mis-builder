# -*- coding: utf-8 -*-
# Copyright 2016-2017 ACSONE SA/NV (<http://acsone.eu>)
# Copyright 2016 Akretion (<http://akretion.com>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


class DataError(Exception):

    def __init__(self, name, msg):
        super(DataError, self).__init__()
        self.name = name
        self.msg = msg


class NameDataError(DataError):
    pass
