Matice sousednosti
==================

Matice sousednosti reprezentuje graf jako čtvercovou matici, kde prvky
reprezentují zda mezi vrcholy v řádku a sloupci existuje hrana.

.. list-table:: Reprezentace druhů grafů
   :widths: 10 50 40
   :header-rows: 1

   * - Druh grafu
     - Popis
     - Příklad
   * - Neorientovaný
     - - :code:`A[v][u] = 0` právě když mezi neexistuje hrana :math:`\{v,u\}`
       - :code:`A[v][u] = 1` právě když mezi existuje hrana :math:`\{v,u\}`
     - .. code-block:: python

          [[ 0, 1, 1, 0],
           [ 1, 0, 0, 0],
           [ 1, 0, 0, 1],
           [ 0, 0, 1, 0]]
   * - Orientovaný
     - Orientovaný graf je reprezentován jako neorientovaný, ale zde se ptáme
       jestli existuje orientovaná hrana :math:`(v, u)` (matice tedy nemusí být symetrická).
     - .. code-block:: python

          [[ 0, 1, 1, 0],
           [ 0, 0, 0, 0],
           [ 0, 0, 0, 1],
           [ 0, 0, 0, 0]]
   * - Obecný (smíšený)
     - Pro prvky matice obecného grafu platí stejná pravidla jako pro
       (ne)orientované grafy dle toho jaká je hrana.
     - .. code-block:: python

          [[ 0, 1, 1, 0],
           [ 0, 0, 0, 0],
           [ 0, 0, 0, 1],
           [ 0, 0, 0, 0]]
   * - Multigraf
     - Pro multigraf není reprezentace implementována.
     -
   * - Ohodnocení vrcholů
     - Ohodnocení vrcholů je reprezentováno separátním seznamem ohodnocení
       indexovaným vrcholy.
     - .. code-block:: python

          [{"color": "red"},
           {"color": "blue"},
           {"color": "red"}]
   * - Ohodnocení hran
     - Ohodnocení hran je reprezentováno separátním seznamem ohodnocení
       indexovaným hranami anebo lze jedno číselné ohodnocení hran reprezentovat
       v matici nahrazením :code:`1` těmito čísly (u neorientovaných hran jsou
       čísla nahrazena symetricky).
     - .. code-block:: python

          [{"length": 52},
           {"length": 36},
           {"length": 11}]
       .. code-block:: python

          [[  0, 75, 32,   0],
           [ 75, 68,  0,   0],
           [  0,  0,  0, -15],
           [  0,  0,  0,   0]]
   * - Obsahující smyčky
     - Platí stejná pravidla jako pro (ne)orientované grafy, ale zde už budou
       :code:`1` i na hlavní diagonále.
     - .. code-block:: python

          [[ 0, 1, 1, 0],
           [ 0, 1, 0, 0],
           [ 0, 0, 1, 1],
           [ 0, 0, 0, 0]]
   * - Hypergraf
     - Reprezentace hypergrafů jako matice sousednosti není implementována ikdyž
       by byla možná například tensorem sousednosti.
     -