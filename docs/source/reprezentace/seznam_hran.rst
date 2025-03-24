Seznam hran
===========

**Seznam hran** reprezentuje graf jako seznam trojic, které reprezentují hrany.
Tyto trojice jsou implementovány pomocí `namedtuple`
:class:`~graph_catalog.constants.EdgeTuple`. Z toho první dva prvky jsou vrcholy
hrany (v orientovaném grafu je první počáteční vrchol a druhý koncový). Třetí
prvek je potom ohodnocení hrany.

Povšimněme si, že tato reprezentace není schopná reprezentovat izolované vrcholy
grafu, protože ukládá pouze hrany a do izolovaného vrcholu žádné nevedou.

Aby jsme odlišili orientované resp. neorientované hrany obsahuje každá hrana
ohodnocení `"directed"` typu `bool` (hrany tedy mají hodnoty `True` resp.
`False`). Smyčky zde uvažujeme jako orientované hrany.

Aby nebyli příklady příliš zahlceny značíme v níže uvedené tabulce
:class:`~graph_catalog.constants.EdgeTuple` jako normální tuply tedy kulatými závorkami.

.. list-table:: Reprezentace druhů grafů
   :widths: 10 50 40
   :header-rows: 1

   * - Druh grafu
     - Popis
     - Příklad
   * - Neorientovaný
     - Neorientované hrany mají ohodnocení `"directed"` rovno `False`.
     - .. code-block:: python
          [
            (0, 1, {"directed": False}),
            (1, 2, {"directed": False}),
            (2, 0, {"directed": False}),
          ]
   * - Orientovaný
     - První vrchol je počáteční a druhý koncový. Neorientované hrany mají ohodnocení `"directed"` rovno `True`.
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
     -
     - ``[(1,2, False),(1,2, False)]``
   * - Ohodnocení vrcholů
     -
     -
   * - Ohodnocení hran
     -
     - ``[(1,2, False, {})]``
   * - Obsahující smyčky
     -
     - ``[(1,1, False, {})]``
   * - Hypergraf
     -
     - ``[([1,1,2,3], [True, False, ...], {})]``