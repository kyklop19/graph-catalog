Reprezentace grafů
==================

.. toctree::
   :maxdepth: 2
   :caption: Obsah:

   seznam_hran
   seznamy_nasledniku
   matice_sousednosti
   matice_incidence
   dynamicka_reprezentace

Jednotlivé grafy mohou mít ohodnocené hrany a vrcholy. Toto ohodnocení je pro
jednotnost pro hranu či vrchol uloženo v :code:`dict`, kde klíčem je název ohodnocení
uložen jako :code:`str` a hodnota může být kteréhokoliv typu.

.. list-table::
   :widths: 75 25
   :header-rows: 1

   * - Reprezentace
     - Typ
   * - :doc:`/reprezentace/seznam_hran`
     - ``EdgeList``
   * - :doc:`/reprezentace/seznamy_nasledniku`
     - ``AdjList``
   * - :doc:`/reprezentace/matice_sousednosti`
     - ``AdjMat``
   * - :doc:`/reprezentace/matice_incidence`
     - ``IncMat``
   * - :doc:`/reprezentace/dynamicka_reprezentace`
     - :class:`graph_catalog.graph.Graph`