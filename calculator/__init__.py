"""
Welcome to super calculator
.. include:: ../README.md
"""

try:
    from .sum import sum
except ModuleNotFoundError:
    print('sum not found')
try:
    from .substraction import substraction
except ModuleNotFoundError:
    print('substraction not found')
try:
    from .multiplication import multiplication
except ModuleNotFoundError:
    print('multiplication not found')
try:
    from .division import division
except ModuleNotFoundError:
    print('division not found')
try:
    from .division_without_remainder import division_without_remainder
except ModuleNotFoundError:
    print('division_without_remainder not found')
try:
    from .reminder import reminder
except ModuleNotFoundError:
    print('reminder not found')
try:
    from .exponentiation import exponentiation
except ModuleNotFoundError:
    print('exponentiation not found')
try:
    from .maximum import maximum
except ModuleNotFoundError:
    print('maximum not found')
try:
    from .minimum import minimum
except ModuleNotFoundError:
    print('minimum not found')
