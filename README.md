<p align="center"><img width="400" src="https://github.com/dmlls/python-casefy/blob/main/docs/source/_static/images/cover.png" alt=""></p>
<p align="center" display="inline-block">
  <a href="https://docs.jizt.it">
    <a href="https://pypi.org/project/casefy/">
      <img src="https://img.shields.io/pypi/v/casefy">
    </a>
    <a href="https://deepsource.io/gh/dmlls/python-casefy/?ref=repository-badge}" target="_blank">
      <img alt="Active Issues" title="DeepSource" src="https://deepsource.io/gh/dmlls/python-casefy.svg/?label=active+issues&token=dbO3UyrUPWvJp6K_PVZpTcnU"/>
    </a>
  </a>
</p>

## Introduction

Casefy (/keɪsfaɪ/) is a lightweight Python package to convert the casing of strings. It has no third-party dependencies and supports Unicode.

<br>

## Installation

The latest release can be installed using [pip](https://pypi.org/project/casefy/):
```shell
pip install -U casefy
```

Casefy is also [available](https://aur.archlinux.org/packages/python-casefy) as an Arch Linux AUR package.

<br>

## Examples

Note: for more details, you can check the [API Reference](https://dmlls.github.io/python-casefy/api.html).

```python
import casefy

# camelCase
string = casefy.camelcase("foo_bar")
print(string)  # fooBar

string = casefy.camelcase("FooBar")
print(string)  # fooBar

string = casefy.camelcase("FOO BAR")
print(string)  # fooBar


# PascalCase
string = casefy.pascalcase("foo_bar")
print(string)  # FooBar

string = casefy.pascalcase("fooBar")
print(string)  # FooBar


# snake_case
string = casefy.snakecase("fooBar")
print(string)  # foo_bar

string = casefy.snakecase("fooBARbaz", keep_together=["bar"])
print(string)  # foo_bar_baz

string = casefy.snakecase("FOO BAR")
print(string)  # foo_bar


# CONST_CASE
string = casefy.constcase("fooBar")
print(string)  # FOO_BAR


# kebab-case
string = casefy.kebabcase("fooBar")
print(string)  # foo-bar


# UPPER-KEBAB-CASE
string = casefy.upperkebabcase("fooBar")
print(string)  # FOO-BAR


# separator case
string = casefy.separatorcase("fooBar", separator="/")
print(string)  # foo/bar

string = casefy.separatorcase("fooBARbaz", separator="%", keep_together=["bar"])
print(string)  # foo%bar%baz


# Sentence case
string = casefy.sentencecase("fooBar")
print(string)  # Foo bar


# Title Case
string = casefy.titlecase("fooBar")
print(string)  # Foo Bar


# Alphanum3ric case (removes non-alphanumeric chars)
string = casefy.alphanumcase("foo - 123 ; bar!")
print(string)  # foo123bar
```

<br>

## Contribute
If you find a bug, please open an issue. Pull Requests are also welcome!

<br>

## Acknowledgements

This project started when I saw that the package [`python-stringcase`](https://aur.archlinux.org/pkgbase/python-stringcase) was flagged-out-of-date in the Arch AUR Repository. The project [stringcase](https://github.com/okunishinishi/python-stringcase) seems not to be actively maintained anymore, so I decided to address its issues and pull requests and solve them in this new package. I kept the API as similar as possible, in order to facilitate any possible migration. I thank [Taka Okunishi](https://github.com/okunishinishi) (author of stringcase) and its contributors for their work.

<br>

## Related projects

- [`case-conversion`](https://github.com/AlejandroFrias/case-conversion) offers a very similar functionality as this project. I probably wouldn't have written this package if I had known of it before. However, the code of Casefy is more lightweight and just enough for most cases. If you need more functionality, e.g., detecting the case of a string, go with `case-conversion`.

- [Inflection](https://github.com/jpvanhal/inflection) presents some overlap with this project as well, allowing the transformation of strings from CamelCase to underscored_string, but also singularizing and pluralizing English words.

<br>

## License
Casefy is distributed under the [MIT](https://github.com/dmlls/python-casefy/blob/main/LICENSE) license.
