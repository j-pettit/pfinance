# pfinance
pfinance is a Python financial mathematics library.
It attempts to provide a comprehensive suite of functions, tools, and calulators geared towards financial applications.
pfinance does not supply APIs for market and exchange lookup.

<table>
  <tr>
    <td>Supports</td>
    <td>Python 3.9</td>
  </tr>
  <tr>
    <td>Latest Release</td>
    <td>
      <a href="https://pypi.org/project/pfinance/">
        <img src="https://img.shields.io/pypi/v/pfinance.svg" alt="latest release" />
      </a>
    </td>
  </tr>
  <tr>
    <td>Package Status</td>
    <td>
      <a href="https://pypi.org/project/pyfinance/">
        <img src="https://img.shields.io/pypi/status/pyfinance.svg" alt="status" /></td>
      </a>
  </tr>
  <tr>
    <td>License</td>
    <td>
      <a href="https://github.com/bsolomon1124/pyfinance/blob/master/LICENSE">
        <img src="https://img.shields.io/pypi/l/pyfinance.svg" alt="license" />
      </a>
    </td>
  </tr>
</table>

## Installation
pfinance is available via [PyPI](https://pypi.python.org/pypi/pfinance/). Install with pip:

```bash
$ python3 -m pip install pfinance
```

**Note**: pfinance requires Python >= 3.9 for full test and annotation compatability, but may offer reduced functionality for earlier 3.x versions.

## Modules
pfinance functions are organized by module.

<table>
  <tr>
    <td>Module</td>
    <td>Description</td>
  </tr>
  <tr>
    <td><code>general</code></td>
    <td>Common finance functions</td>
  </tr>
  <tr>
    <td><code>depreciation</code></td>
    <td>Depreciation of assets functions</td>
  </tr>
  <tr>
    <td><code>time_value</code></td>
    <td>Time value of money functions</td>
  </tr>
  <tr>
    <td><code>conversion</code></td>
    <td>Unit and notation conversion functions</td>
  </tr>
  <tr>
    <td><code>securities</code></td>
    <td>Securities tracking and analysis functions</td>
  </tr>
</table>

## Example
Determine the value of a $100.00 investment earning 7% interest compounded monthly after 10 years.
```python
>>> from pfinance import general
>>> value = general.compound_interest(100, 0.07, 10, 12)
>>> print(round(value, 2))
200.97
```

## Dependencies

pfinance does not rely on any third party dependencies.
