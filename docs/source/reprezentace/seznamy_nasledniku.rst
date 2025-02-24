Seznamy následníků
==================

**Seznamy následníků** reprezentují graf jako seznam indexovaný vrcholy, kde
každý prvek je seznam obsahující dvojice. První prvek dvojice je vrchol, do
kterého vede hrana z vrcholu, který je indexem tohoto seznamu dvojic. Druhý
prvek je potom ohodnocení hrany.

Dvojice reprezentující následníka je implementována pomocí :code:`namedtuple`
:class:`graph_catalog.constants.NbrTuple` (prvky jsou tedy přístupné pod
indexem, ale také jako aliasy). V níže uvedené tabulce je však budeme značit
jako normální tuply kulatými závorkami.

V této reprezentaci je složité odlišit orientované a neorientované grafy/hrany.
Abychom mohli reprezentovat neorientované hrany musíme předpokládat, že pokud
existuje orientovaná hrana mezi dvěma vrcholy a navíc existuje obrácená hrana
mezi stejnými vrcholy, tak je to neorientovaná hrana.

Pro jednoznačnost reprezentace mají hrany hrany ohodnocení :code:`"index"`.
Každá hrana grafu má tedy jiné číslo. Neorientovaná hrana je potom
reprezentována dvěmi protichůdně vedoucími hranami mezi stejnými vrcholy se
stejným indexem.

.. list-table:: Reprezentace druhů grafů
   :widths: 10 50 40
   :header-rows: 1

   * - Druh grafu
     - Popis
     - Příklad
   * - Neorientovaný
     - Neorientovaná hrana je reprezentována dvěmi protichůdně vedoucími
       hranami mezi stejnými vrcholy se stejným indexem.
     - .. code-block:: python

          [[(1, {"index": 0}), (2, {"index": 1})],
           [(0, {"index": 0})],
           [(0, {"index": 1})]]
   * - Orientovaný
     - Orientovaná hrana je tvoří dvojice reprezentující následníka s unikátním indexem.
     - .. code-block:: python

          [[(1, {"index": 0}), (2, {"index": 1})],
           [],
           []]
   * - Obecný (smíšený)
     - Pro hrany obecného grafu platí stejná pravidla jako pro (ne)orientované
       grafy dle hrany.
     - .. code-block:: python

          [[(1, {"index": 0}), (2, {"index": 1})],
           [(0, {"index": 0})],
           []]
   * - Multigraf
     - Každá hrana do stejného následníka má jiný index.
     - .. code-block:: python

          [[(1, {"index": 0}), (1, {"index": 1})],
           [(0, {"index": 0}), (0, {"index": 1})],
           []]
   * - Ohodnocení vrcholů
     - Ohodnocení vrcholů je reprezentováno separátním seznamem ohodnocení
       indexovaným vrcholy.
     - .. code-block:: python

          [{"color": "red"},
           {"color": "blue"},
           {"color": "red"}]
   * - Ohodnocení hran
     - Druhý prvek ve dvojici reprezentující následníka je ohodnocení hrany.
       Neorientované hrany mají v obou dvojicích stejné ohodnocení.
     - .. code-block:: python

          [[(1, {"index": 0, "length": 56}), (2, {"index": 1, "length": 11})],
           [(0, {"index": 0, "length": 56})],
           []]
   * - Obsahující smyčky
     - Index následníka je stejný jako index počátečního vrcholu
     - .. code-block:: python

          [[(1, {"index": 0}), (0, {"index": 1})],
           [(0, {"index": 0})],
           []]
   * - Hypergraf
     - Pro hypergraf není reprezentace implementována.
     -