"""
This module contains the UDFs for the project.
"""

def combine(string_a: str, string_b: str) -> str:
    """
    A sample UDF implementation
    """

    return string_a + string_b

def combine_sizes(length: float, width: float) -> str:
    """
    A sample UDF implementation
    """

    return str(length) + "cm x " + str(width) + "cm"
