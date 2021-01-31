"""
Easily review dependencies between SQL Transformations

Copyright: (c) 2021, Moritz Eilfort
GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""

__version__ = "0.0.0"
__author__ = "Moritz Eilfort"
__author_email__ = "britz@jimfawkes.com"
__url__ = "github.com/JimFawkes/britz"
__license__ = "GPLv3+"
__copyright__ = f"Copyright 2021 {__author__}"

# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler

logging.getLogger("britz").addHandler(NullHandler())
