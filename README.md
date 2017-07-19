Sugar Toolkit
=============

Sugar Toolkit provides services and a set of GTK+ widgets to build
activities and other Sugar components on Linux based computers.

This is the GTK+ 2 binding of the Sugar Toolkit.

This is deprecated for new activities; please use [Sugar Toolkit for
GTK+ 3](https://github.com/sugarlabs/sugar-toolkit-gtk3); but several
activities still use GTK+ 2 and so some maintenance does occur here.

https://www.sugarlabs.org/

https://wiki.sugarlabs.org/

Installing on Debian or Ubuntu
------------------------------

Automatically done when you install [Sugar
desktop](https://github.com/sugarlabs/sugar).

To install Sugar Toolkit alone without Sugar desktop,

```
sudo apt install python-sugar
```

Installing on Fedora
--------------------

Automatically done when you install [Sugar
desktop](https://github.com/sugarlabs/sugar).

To install Sugar Toolkit alone without Sugar desktop,

```
sudo dnf install sugar-toolkit
```

Building
--------

Sugar Toolkit follows the [GNU Coding
Standards](https://www.gnu.org/prep/standards/).

Install all dependencies, especially sugar-artwork and
sugar-datastore.

Clone the repository, run `autogen.sh`, then `make` and `make
install`.
