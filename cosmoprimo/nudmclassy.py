"""Cosmological calculation with the Boltzmann code NuDMCLASS."""

from pyclass import nudmclass

from .cosmology import BaseEngine, CosmologyInputError, CosmologyComputationError
from . import classy


class NuDMClassEngine(classy.ClassEngine):

    """Engine for the Boltzmann code nudmclass."""

    name = 'nudmclass'

    _default_cosmological_parameters = dict()
    _check_ignore = ['m_ncdm']

    def _set_classy(self, params):

        class _ClassEngine(nudmclass.ClassEngine):

            def compute(self, tasks):
                try:
                    return super(_ClassEngine, self).compute(tasks)
                except nudmclass.ClassInputError as exc:
                    raise CosmologyInputError from exc
                except nudmclass.ClassComputationError as exc:
                    raise CosmologyComputationError from exc

        self.classy = _ClassEngine(params=params)


class Background(classy.BaseClassBackground, nudmclass.Background):

    """Your modifications, if any."""


class Thermodynamics(classy.BaseClassThermodynamics, nudmclass.Thermodynamics):

    """Your modifications, if any."""


class Primordial(classy.BaseClassPrimordial, nudmclass.Primordial):

     """Your modifications, if any."""


class Perturbations(classy.BaseClassPerturbations, nudmclass.Perturbations):

     """Your modifications, if any."""


class Transfer(classy.BaseClassTransfer, nudmclass.Transfer):

     """Your modifications, if any."""


class Harmonic(classy.BaseClassHarmonic, nudmclass.Harmonic):
     """Your modifications, if any."""


class Fourier(classy.BaseClassFourier, nudmclass.Fourier):
     """Your modifications, if any."""
