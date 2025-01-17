# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:05:22 2021

@author: wantysal
"""
# Optional package import
try:
    import SciDataTool
except ImportError:
    SciDataTool = None

# Import MOSQITO function
from mosqito.functions.roughness_danielweber.comp_roughness import comp_roughness


def compute_roughness(self, method="dw", overlap=0.5):
    """Method to compute roughness according to the Daniel and Weber implementation

    Parameter
    ---------
    method : string
        method used to do the computation 'danielweber' is the only one for now
    overlap : float
        overlapping coefficient for the time windows of 200ms, default is 0.5
    """

    if SciDataTool is None:
        raise RuntimeError(
            "In order to create an audio object you need the 'SciDataTool' package."
            )

    # check the input parameters
    if method != "dw":
        raise ValueError("ERROR: method must be 'dw'")

    if overlap < 0 or overlap > 1:
        raise ValueError("ERROR: overlap value must be between 0 and 1")

    R = comp_roughness(self.signal.values, self.fs, overlap)

    time = SciDataTool.Data1D(name="time", unit="s", values=R["time"])

    self.roughness["Daniel Weber"] = SciDataTool.DataTime(
        symbol="R_{dw}",
        axes=[time],
        values=R["values"],
        name="Roughness",
        unit="Asper",
    )
