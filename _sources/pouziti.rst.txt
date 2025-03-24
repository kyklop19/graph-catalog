Použití
=======

Načtení grafu z katalogu
------------------------

Knihovna poskytuje vestavěný katalog grafů, kde každý graf je identifikován
jedinečným jménem resp. číslem ve formátu "<číslo>.<číslo>". Pro načítání grafů
dle jednotlivých identifikátorů slouží funkce :func:`~graph_catalog.catalog.load_with_name`
resp. :func:`~graph_catalog.catalog.load_with_number`. Obě vracejí `dict` s grafem a dalšími
daty o něm. Ovšem :func:`~graph_catalog.catalog.load_with_number` nevrací všechna data, aby
graf zůstal více anonymní.

Katalog si můžete prohlédnout :doc:`zde</katalog/index>`.

.. code-block:: python

    from graph_catalog.catalog import load_with_name, load_with_number

    graph_data = load_with_name("1.0")

Převody grafů mezi reprezentacemi
---------------------------------

Při načítání grafů obě funkce vrací graf jako
:doc:`/reprezentace/matice_incidence` ovšem pro práci s grafy tato reprezentace
nemusí být nejvhodnější. Proto tato knihovna poskytuje package
:doc:`/modules/conversion/index`, zahrnující funkce pro převod z jedné
reprezentace do druhé.

Pokud máme `reprezentaci1`, tak pro převod do `reprezentace2` importujeme z
`conversion.from_<reprezentace_1>` funkci `<Reprezentace1>2<Reprezentace2>`
(viz. příklad níže).

Pro více informací o reprezentacích nahlédněte do :doc:`/reprezentace/index`.

.. code-block:: python

    from graph_catalog.catalog import load_with_number
    from graph_catalog.conversion.from_inc_mat import IncMat2AdjList

    graph_data = load_with_number("1.0")
    graph = IncMat2AdjList(graph_data["graph"]) # převod do seznamů následníků

Ukázkové funkce
---------------

Po převodu je s grafem možné provádět různé úkony. Proto knihovna pro ukázku
zpracování grafů poskytuje package :doc:`/modules/algorithms/index`, který dle
kategorie úkonu obsahuje popisně pojmenované subpackage (e.g.
:doc:`/modules/algorithms/searching` pro prohledávání grafu).

Pro ukázku je tu kód pro prohledání grafu za pomocí depth-first searche a
vypsání vrcholů.

.. testcode::

    from graph_catalog.catalog import load_with_number
    from graph_catalog.conversion.from_inc_mat import IncMat2AdjList
    from graph_catalog.algorithms.searching import dfs

    graph_data = load_with_number("1.0")
    graph = IncMat2AdjList(graph_data["graph"])

    for vertex, __ in dfs(graph, graph_data["root"]):
        print(vertex)

Výstup:

.. testoutput::

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
