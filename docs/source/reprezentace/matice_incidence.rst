Matice incidence
================

**Matice incidence** je implementována jako 2 vnořené seznamy resp. matice, kde
členy jsou celá čísla. Řádky reprezentují vrcholu a sloupce hrany.

Tato reprezentace je vnitřně použita pro ukládání grafů v katalogu a při jejich
načítání je vrácena funkcí :func:`graph_catalog.catalog.load`. Důvodem je, že
dokáže dobře popsat všechny druhy grafů.

Zvolení řádků jako vrcholů je z důvodu možnosti reprezentace prázdného grafu
(grafu s určitým počtem vrcholů a bez hran). Kdybychom volili hrany, tak bychom
neměli řádky, tudíž bychom měli prázdný list a nevěděli bychom počet vrcholů.
Takto máme list s určitým počtem prázdných listů.

.. list-table:: Reprezentace druhů grafů
   :widths: 10 50 40
   :header-rows: 1

   * - Druh grafu
     - Popis
     - Příklad
   * - Neorientovaný
     -  - :code:`A[v][e] = 0` právě když vrchol :code:`v` **neleží** na hraně :code:`e`
        - :code:`A[v][e] = 1` právě když vrchol :code:`v` **leží** na hraně :code:`e`
     - .. code-block:: python

          [[ 1, 0, 0, 1, 0],
           [ 0, 1, 0, 1, 0],
           [ 1, 0, 1, 0, 0]]
   * - Orientovaný
     -  - :code:`A[v][e] = 0` právě když vrchol :code:`v` **neleží** na hraně :code:`e`
        - :code:`A[v][e] = +1` právě když vede hrana :code:`e` **z** vrcholu :code:`v`
        - :code:`A[v][e] = -1` právě když vede hrana :code:`e` **do** vrcholu :code:`v`
     - .. code-block:: python

          [[ 1, 0, 0, 1, 0],
           [ 0, 1, 0, 1, 0],
           [ 1, 0, 1, 0, 0]]
   * - Obecný (smíšený)
     - V obecném grafu jsou hrany reprezentovány buď jako v neorientovaném nebo
       jako v orientovaném.

       - neorientované hrany se skládají z dvou :code:`1` a jinak samých :code:`0`
       - orientované hrany se skládají z jedné :code:`1`, jedné :code:`-1` a jinak samých :code:`0`
     - .. code-block:: python

          [[ 1, 0, 0,-1, 0],
           [ 0, 1, 0, 1, 0],
           [-1, 0, 1, 0, 0]]
   * - Multigraf
     - Více násobné hrany jsou v matici vícekrát
     - .. code-block:: python
          :emphasize-lines: 2,3

          [[ 1, 0, 0,-1, 0]
           [ 0, 1, 0, 1, 0]
           [ 0, 1, 0, 1, 0]
           [-1, 0, 1, 0, 0]
           [-1, 0, 1, 0, 0]]
   * - Ohodnocení vrcholů
     - Ohodnocení vrcholů je reprezentováno separátním seznamem ohodnocení
       indexovaným vrcholy.
     - .. code-block:: python

          [{"color": "red"},
           {"color": "blue"},
           {"color": "red"}]
   * - Ohodnocení hran
     - Ohodnocení hran je reprezentováno separátním seznamem ohodnocení
       indexovaným hranami.
     - .. code-block:: python

          [{"length": 52},
           {"length": 36},
           {"length": 11}]
   * - Obsahující smyčky
     - - :code:`A[v][e] = 0` právě když vrchol :code:`v` **neleží** na hraně :code:`e`
       - :code:`A[v][e] = 2` právě když vrchol :code:`v` **má** smyčku :code:`e`
     - .. code-block:: python
          :emphasize-lines: 2

          [[ 1, 0, 1],
           [ 0, 2, 0]]
   * - Hypergraf
     - Hyperhrany jsou dle orientovanosti reprezentovány stejně jako v obecném
       grafu, ale incidentních může být více vrcholů (tedy hrana může mít více
       :code:`1`/:code:`-1`). Graf může taky obsahovat smyčky stejně jako v
       předchozím případě.
     - .. code-block:: python

          [[ 1, 1, 1, 0],
           [ 0, 2, 0, 0],
           [ 0, 1, 1, -1]]