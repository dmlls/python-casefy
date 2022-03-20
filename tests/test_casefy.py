"""Tests for casefy."""

__version__ = "0.1.2"


import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.resolve()))
import casefy


def main():
    """Tests."""
    # camelCase
    assert "fooBar" == casefy.camelcase("foo_bar")
    assert "fooBar" == casefy.camelcase("FooBar")
    assert "fooBar" == casefy.camelcase("FOO BAR")
    assert "fooBar" == casefy.camelcase("foo bar")
    assert "fooBar2" == casefy.camelcase("foo_bar_2")
    assert "foo2Bar" == casefy.camelcase("foo2bar")
    assert "foo2Bar" == casefy.camelcase("foo2Bar")
    assert "foo2Bar2" == casefy.camelcase("foo2Bar2")
    assert "fooB2Bar2" == casefy.camelcase("FooB2_Bar2")
    assert "fooBar" == casefy.camelcase("FooBar")
    assert "fooBar" == casefy.camelcase("FOO BAR")
    assert "fooBar" == casefy.camelcase("foo-bar")
    assert "fooBar" == casefy.camelcase("foo.bar")
    assert "barBaz" == casefy.camelcase("_bar_baz")
    assert "barBaz" == casefy.camelcase(".bar_baz")
    assert "" == casefy.camelcase("----")
    assert "" == casefy.camelcase("")
    assert "" == casefy.camelcase(None)

    # PascalCase
    assert "FooBar" == casefy.pascalcase("foo_bar")
    assert "FooBar" == casefy.pascalcase("FooBar")
    assert "FooBar" == casefy.pascalcase("FOO BAR")
    assert "FooBar" == casefy.pascalcase("foo bar")
    assert "FooBar2" == casefy.pascalcase("foo_bar_2")
    assert "Foo2Bar" == casefy.pascalcase("foo2bar")
    assert "Foo2Bar" == casefy.pascalcase("foo2Bar")
    assert "Foo2Bar2" == casefy.pascalcase("foo2Bar2")
    assert "FooB2Bar2" == casefy.pascalcase("FooB2_Bar2")
    assert "FooBar" == casefy.pascalcase("FooBar")
    assert "FooBar" == casefy.pascalcase("foo-bar")
    assert "FooBar" == casefy.pascalcase("foo.bar")
    assert "BarBaz" == casefy.pascalcase("_bar_baz")
    assert "BarBaz" == casefy.pascalcase(".bar_baz")
    assert "" == casefy.pascalcase("----")
    assert "" == casefy.pascalcase("")
    assert "" == casefy.pascalcase(None)

    # snake_case
    assert "foo_bar" == casefy.snakecase("fooBar")
    assert "foo_bar" == casefy.snakecase("FooBar")
    assert "foo_bar" == casefy.snakecase("FOO BAR")
    assert "foo_bar" == casefy.snakecase("foo bar")
    assert "foo_bar_baz" == casefy.snakecase("fooBARbaz", keep_together=["BAR"])
    assert "foo_bar_2" == casefy.snakecase("fooBar2")
    assert "foo_2_bar" == casefy.snakecase("foo2bar")
    assert "foo_2_bar" == casefy.snakecase("foo2Bar")
    assert "foo_2_bar_2" == casefy.snakecase("foo2Bar2")
    assert "foo_b_2_bar_2" == casefy.snakecase("FooB2_Bar2")
    assert "foo_bar" == casefy.snakecase("foo_bar")
    assert "foo_bar" == casefy.snakecase("foo-bar")
    assert "foo_bar" == casefy.snakecase("foo.bar")
    assert "_bar_baz" == casefy.snakecase("_bar_baz")
    assert "bar_baz" == casefy.snakecase(".bar_baz")
    assert "" == casefy.snakecase("")
    assert "" == casefy.snakecase(None)

    # CONST_CASE
    assert "FOO_BAR" == casefy.constcase("fooBar")
    assert "FOO_BAR" == casefy.constcase("FooBar")
    assert "FOO_BAR" == casefy.constcase("FOO BAR")
    assert "FOO_BAR" == casefy.constcase("foo bar")
    assert "FOO_BAR_2" == casefy.constcase("fooBar2")
    assert "FOO_2_BAR" == casefy.constcase("foo2bar")
    assert "FOO_2_BAR" == casefy.constcase("foo2Bar")
    assert "FOO_2_BAR_2" == casefy.constcase("foo2Bar2")
    assert "FOO_B_2_BAR_2" == casefy.constcase("FooB2_Bar2")
    assert "FOO_BAR" == casefy.constcase("foo_bar")
    assert "FOO_BAR" == casefy.constcase("foo-bar")
    assert "FOO_BAR" == casefy.constcase("foo.bar")
    assert "_BAR_BAZ" == casefy.constcase("_bar_baz")
    assert "BAR_BAZ" == casefy.constcase(".bar_baz")
    assert "" == casefy.constcase("")
    assert "" == casefy.constcase(None)

    # kebab-case
    assert "foo-bar" == casefy.kebabcase("fooBar")
    assert "foo-bar" == casefy.kebabcase("FooBar")
    assert "foo-bar" == casefy.kebabcase("FOO BAR")
    assert "foo-bar" == casefy.kebabcase("foo bar")
    assert "foo-bar-2" == casefy.kebabcase("fooBar2")
    assert "foo-2-bar" == casefy.kebabcase("foo2bar")
    assert "foo-2-bar" == casefy.kebabcase("foo2Bar")
    assert "foo-2-bar-2" == casefy.kebabcase("foo2Bar2")
    assert "foo-b-2-bar-2" == casefy.kebabcase("FooB2_Bar2")
    assert "foo-bar" == casefy.kebabcase("foo_bar")
    assert "foo-bar" == casefy.kebabcase("foo-bar")
    assert "foo-bar" == casefy.kebabcase("foo.bar")
    assert "bar-baz" == casefy.kebabcase("_bar_baz")
    assert "bar-baz" == casefy.kebabcase(".bar_baz")
    assert "" == casefy.kebabcase("")
    assert "" == casefy.kebabcase(None)

    # UPPER-KEBAB-CASE
    assert "FOO-BAR" == casefy.upperkebabcase("fooBar")
    assert "FOO-BAR" == casefy.upperkebabcase("FooBar")
    assert "FOO-BAR" == casefy.upperkebabcase("FOO BAR")
    assert "FOO-BAR" == casefy.upperkebabcase("foo bar")
    assert "FOO-BAR-2" == casefy.upperkebabcase("fooBar2")
    assert "FOO-2-BAR" == casefy.upperkebabcase("foo2bar")
    assert "FOO-2-BAR" == casefy.upperkebabcase("foo2Bar")
    assert "FOO-2-BAR-2" == casefy.upperkebabcase("foo2Bar2")
    assert "FOO-B-2-BAR-2" == casefy.upperkebabcase("FooB2_Bar2")
    assert "FOO-BAR" == casefy.upperkebabcase("foo_bar")
    assert "FOO-BAR" == casefy.upperkebabcase("foo-bar")
    assert "FOO-BAR" == casefy.upperkebabcase("foo.bar")
    assert "BAR-BAZ" == casefy.upperkebabcase("_bar_baz")
    assert "BAR-BAZ" == casefy.upperkebabcase(".bar_baz")
    assert "" == casefy.upperkebabcase("")
    assert "" == casefy.upperkebabcase(None)

    # separator case
    assert "foo.bar" == casefy.separatorcase("fooBar", separator=".")
    assert "foo/bar/baz" == casefy.separatorcase(
        "fooBARbaz", separator="/", keep_together=["BAR"])
    assert r"foo%bar%2" == casefy.separatorcase("fooBar2", separator="%")
    assert "foo&2&bar" == casefy.separatorcase("foo2Bar", separator="&")
    assert "foo?bar" == casefy.separatorcase("foo_bar", separator="?")
    assert "foo#bar" == casefy.separatorcase("foo-bar", separator="#")
    assert "foo=bar" == casefy.separatorcase("foo.bar", separator="=")
    assert "@bar@baz" == casefy.separatorcase("_bar_baz", separator="@")
    assert "#!bar#!baz" == casefy.separatorcase(".bar_baz", separator="#!")
    assert "" == casefy.separatorcase("", separator="")
    assert "" == casefy.separatorcase(None, separator="")

    # Sentence case
    assert "Foo bar" == casefy.sentencecase("fooBar")
    assert "Foo bar" == casefy.sentencecase("foo bar")
    assert "Foo bar" == casefy.sentencecase("foo_bar")
    assert "Foo bar" == casefy.sentencecase("foo-bar")
    assert "Foo bar" == casefy.sentencecase("foo.bar")
    assert "Bar baz" == casefy.sentencecase("_bar_baz")
    assert "Bar baz" == casefy.sentencecase(".bar_baz")
    assert "" == casefy.sentencecase("")
    assert "" == casefy.sentencecase(None)

    # Title Case
    assert "Foo Bar" == casefy.titlecase("fooBar")
    assert "Foo Bar 2" == casefy.titlecase("fooBar2")
    assert "Foo 2 Bar" == casefy.titlecase("foo2Bar")
    assert "Foo Bar" == casefy.titlecase("foo_bar")
    assert "Foo Bar" == casefy.titlecase("foo-bar")
    assert "Foo Bar" == casefy.titlecase("foo.bar")
    assert "Bar Baz" == casefy.titlecase("_bar_baz")
    assert "Bar Baz" == casefy.titlecase(".bar_baz")
    assert "" == casefy.titlecase("")
    assert "" == casefy.titlecase(None)

    # Alphanumeric case
    assert "FooBar" == casefy.alphanumcase("_Foo., Bar")
    assert "Foo123Bar" == casefy.alphanumcase("Foo_123 Bar!")
    assert "" == casefy.alphanumcase("")
    assert "" == casefy.alphanumcase(None)

    # lowercase
    assert "foobar" == casefy.lowercase("foobar")
    assert "foobar" == casefy.lowercase("fooBar")
    assert "foo_bar" == casefy.lowercase("foo_bar")
    assert "" == casefy.lowercase("")
    assert "" == casefy.lowercase(None)

    # UPPERCASE
    assert "FOOBAR" == casefy.uppercase("foobar")
    assert "FOOBAR" == casefy.uppercase("fooBar")
    assert "FOO_BAR" == casefy.uppercase("foo_bar")
    assert "" == casefy.uppercase("")
    assert "" == casefy.uppercase(None)

    # CapitalCase
    assert "Foobar" == casefy.capitalcase("foobar")
    assert "FooBar" == casefy.capitalcase("fooBar")
    assert "" == casefy.capitalcase("")
    assert "" == casefy.capitalcase(None)

    print("OK")


if __name__ == "__main__":
    main()
