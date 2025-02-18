Matice incidence
================

**Matice incidence** je implementována jako 2 vnořené seznamy resp. matice, kde
členy jsou celá čísla. Řádky reprezentují hrany a sloupce vrcholy.

.. list-table:: Reprezentace druhů grafů
   :widths: 20 40 40
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
     - .. code-block:: python

          [[ 1, 0, 0,-1, 0]
           [ 0, 1, 0, 1, 0]
           [-1, 0, 1, 0, 0]
           [ 0, 1, 0, 1, 0]]
   * - Multigraf
     - 
     - .. code-block:: python
          :emphasize-lines: 2,3

          [[ 1, 0, 0,-1, 0]
           [ 0, 1, 0, 1, 0]
           [ 0, 1, 0, 1, 0]
           [-1, 0, 1, 0, 0]
           [-1, 0, 1, 0, 0]]
   * - Ohodnocení vrcholů
     - 
     - 
   * - Ohodnocení hran
     - 
     - 
   * - Obsahující smyčky
     - 
     - .. code-block:: python
          :emphasize-lines: 2

          [[ 1, 0, 1]
           [ 0, 2, 0]]
   * - Hypergraf
     - 
     - .. code-block:: python

          [[ 1, 0, 1]
           [ 1, 2, 1]]