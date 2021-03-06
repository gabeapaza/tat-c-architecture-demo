#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Object models and methods for managing space system instruments.
"""

import json

from .util import Entity
from .agency import Agency

class Instrument(Entity):
    """A payload component that performs scientific observation functions.

    Attributes:
        name        Full name of this launch vehicle.
        acronym     Acronym, initialism, or abbreviation.
        agency      Designer, provider, or operator of this entity.
        mass        Total mass (kg) of this entity including any consumable
                    propellants or gases.
        volume      Total volume (m3) of this entity.
        power       Nominal operating power (W).
        operatingWavelength     Wavelength (nm) of measured electromagnetic
                    spectra.
        pixelBitDepth   Number of bits recorded per pixel.
        fieldOfView     Angular dimension (degrees) of the extent of a
                    completed image (i.e. half-angle) in the cross-track
                    direction (orthogonal to orbital motion).
        numberPixels    Number of pixels for a completed image in the
                    cross-track direction (orthogonal to orbital motion).
        dataRate        Rate of data recorded (Mbps) during nominal operations.
        solarConditions     Required solar conditions during operations.
                    Recognized values include: SUNLIT, ECLIPSE.
    """

    def __init__(self, name=None, acronym=None, agency=None, mass=None,
            volume=None, power=None, operatingWavelength=None, pixelBitDepth=None,
            fieldOfView=None, numberPixels=None, dataRate=None,
            solarConditions=None, _id=None):
        """Initialize an instrument object.
        """
        self.name = name
        self.acronym = acronym if acronym else name
        self.agency = agency
        self.mass = mass
        self.volume = volume
        self.power = power
        self.operatingWavelength = operatingWavelength
        self.pixelBitDepth = pixelBitDepth
        self.fieldOfView = fieldOfView
        self.numberPixels = numberPixels
        self.dataRate = dataRate
        self.solarConditions = solarConditions
        super(Instrument,self).__init__(_id, "Instrument")

    @staticmethod
    def from_dict(d):
        """Parses an instrument from a normalized JSON dictionary."""
        return Instrument(
                name = d.get("name", None),
                acronym = d.get("acronym", None),
                agency = Agency.from_json(d.get("agency", None)),
                mass = d.get("mass", None),
                volume = d.get("volume", None),
                power = d.get("power", None),
                operatingWavelength = d.get("operatingWavelength", None),
                pixelBitDepth = d.get("pixelBitDepth", None),
                fieldOfView = d.get("fieldOfView", None),
                numberPixels = d.get("numberPixels", None),
                dataRate = d.get("dataRate", None),
                solarConditions = d.get("solarConditions", None),
                _id = d.get("@id", None)
            )
