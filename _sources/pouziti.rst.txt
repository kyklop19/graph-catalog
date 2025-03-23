Použití
=======

Načtení grafu z katalogu
------------------------

Knihovna poskytuje vestavěný katalog grafů, kde každý graf je identifikován
jedinečným jménem resp. číslem ve formátu "<číslo>.<číslo>". Pro načítání grafů
dle jednotlivých identifikátorů slouží funkce :func:`catalog.load_with_name`
resp. :func:`catalog.load_with_number`. Obě vracejí `dict` s grafem a dalšími
daty o něm. Ovšem :func:`catalog.load_with_number` nevrací všechna data, aby
graf zůstal více anonymní.

.. code-block:: python

    from graph_catalog.catalog import load_with_name, load_with_number

    load_with_name("")

Převody grafů mezi reprezentacemi
---------------------------------

.. code-block:: python

    from graph_catalog.conversion.from_inc_mat import IncMat2AdjList

Ukázkové funkce
---------------

.. code-block:: python

    from graph_catalog.algorithms.searching import dfs