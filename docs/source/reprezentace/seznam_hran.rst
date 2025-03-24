Seznam hran
===========

**Seznam hran** reprezentuje graf jako seznam trojic, které reprezentují hrany.
Tyto trojice jsou implementovány pomocí ``namedtuple``
:class:`~graph_catalog.constants.EdgeTuple`. Z toho první dva prvky jsou vrcholy
hrany (v orientovaném grafu je první počáteční vrchol a druhý koncový). Třetí
prvek je potom ohodnocení hrany.

Povšimněme si, že tato reprezentace není schopná reprezentovat izolované vrcholy
grafu, protože ukládá pouze hrany a do izolovaného vrcholu žádné nevedou.

Aby jsme odlišili orientované resp. neorientované hrany obsahuje každá hrana
ohodnocení ``"directed"`` typu ``bool`` (hrany tedy mají hodnoty ``True`` resp.
``False``). Smyčky zde uvažujeme jako orientované hrany.

Aby nebyli příklady příliš zahlceny značíme v níže uvedené tabulce
:class:`~graph_catalog.constants.EdgeTuple` jako normální tuply tedy kulatými závorkami.

.. list-table:: Reprezentace druhů grafů
   :widths: 10 50 40
   :header-rows: 1

   * - Druh grafu
     - Popis
     - Příklad
   * - Neorientovaný
     - Neorientované hrany mají ohodnocení ``"directed"`` rovno ``False``.
     - .. code-block:: python

          [
            (0, 1, {"directed": False}),
            (1, 2, {"directed": False}),
            (2, 0, {"directed": False}),
          ]
   * - Orientovaný
     - První vrchol je počáteční a druhý koncový. Neorientované hrany mají ohodnocení ``"directed"`` rovno ``True``.
     - .. code-block:: python

          [
            (0, 1, {"directed": True}),
            (1, 2, {"directed": True}),
            (2, 0, {"directed": True}),
          ]
   * - Obecný (smíšený)
     - V tomto případě je obecný graf kombinace pravidel pro orientované a
       neorientované grafy.
     - .. code-block:: python

          [
            (0, 1, {"directed": True}),
            (1, 2, {"directed": False}),
            (2, 0, {"directed": False}),
          ]
   * - Multigraf
     - Více hran mezi stejnými vrcholy je jednoduše reprezentován více tuply v
       seznamu se stejnými vrcholy.
     - .. code-block:: python
          :emphasize-lines: 2-3

          [
            (0, 1, {"directed": True}),
            (0, 1, {"directed": False}),
            (1, 2, {"directed": False}),
          ]
   * - Ohodnocení vrcholů
     - Ohodnocení vrcholů je reprezentováno separátním seznamem ohodnocení
       indexovaným vrcholy.
     - .. code-block:: python

          [{"color": "red"},
           {"color": "blue"},
           {"color": "red"}]
   * - Ohodnocení hran
     - Každá hrana má svoje ohodnocení jako třetí prvek.
     - .. code-block:: python

          [
            (0, 1, {"directed": True, "length": 52}),
            (1, 2, {"directed": False, "length": 3}),
            (2, 0, {"directed": False, "length": 96}),
          ]
   * - Obsahující smyčky
     - Smyčky jsou reprezentovány stejnými dvěma vrcholy a jsou orientované.
     - .. code-block:: python
          :emphasize-lines: 2

          [
            (0, 0, {"directed": True}),
            (1, 2, {"directed": False}),
            (2, 0, {"directed": False}),
          ]
   * - Hypergraf
     - Pro hypergraf není reprezentace implementována.
     -