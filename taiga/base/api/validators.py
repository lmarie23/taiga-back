# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import re

from django.conf import settings
from django.utils.translation import ugettext as _
from django.core import validators as core_validators
from taiga.base.exceptions import ValidationError
from . import serializers


class Validator(serializers.Serializer):
    pass


class ModelValidator(serializers.ModelSerializer):
    pass


class PasswordValidator(Validator):
    password = serializers.CharField()

    def validate_password(self, attrs, source):
        value = attrs[source]
        validator = core_validators.RegexValidator(re.compile(settings.PASSWORD_VALIDATOR_REGEX),
                                                   _("invalid password"), "invalid")

        try:
            validator(value)
        except ValidationError:
            raise ValidationError(_("Required. Ask your Taiga system administrators for details."))
        return attrs
