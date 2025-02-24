Seznam hran
===========

**Seznam hran** reprezentuje graf jako seznam trojic, které reprezentují hrany.

.. list-table:: Reprezentace druhů grafů
   :widths: 10 50 40
   :header-rows: 1

   * - Druh grafu
     - Popis
     - Příklad
   * - Neorientovaný
     -
     -
   * - Orientovaný
     -
     -
   * - Obecný (smíšený)
     -
     - ``[(1,2, False),(3,4, True)]``
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