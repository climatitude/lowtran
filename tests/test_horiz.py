#!/usr/bin/env python
import pytest
import lowtran
from pytest import approx


def test_horiz():
    c1 = {'zmdl': 0.3,
          'h1': 0.3,
          'range_km': 1.,
          'wlshort': 200.,
          'wllong': 30000.,
          'wlstep': 20.,
          }

    TR = lowtran.horiztrans(c1)

    assert TR.wavelength_nm[[0, -1]].values == approx((30303.03, 200), rel=0.001)
    assert TR['transmission'][0, [1000, 1200], 0].values == approx([0.980679, 0.959992], rel=0.001)


def test_userhoriz():

    c1 = {'zmdl': 0.3,
          'h1': 0.3,
          'range_km': 1.,
          'wlshort': 200.,
          'wllong': 30000.,
          'wlstep': 20.,
          }

    atmos = {'p': 949., 't': 283.8, 'wmol': [93.96, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]}

    c1.update(atmos)

    TR = lowtran.userhoriztrans(c1)

    assert TR.wavelength_nm[[0, -1]].values == approx((30303.03, 200), rel=0.001)
    assert TR['transmission'][0, [1000, 1200], 0].values == approx([0.982909, 0.9645], rel=0.001)


if __name__ == '__main__':
    pytest.main([__file__])
