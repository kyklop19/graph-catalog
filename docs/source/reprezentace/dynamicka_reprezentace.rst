Dynamická reprezentace
======================

Dynamická reprezentace je implementovaná jako třída
:class:`~graph_catalog.graph.Graph`, kde vrcholy a hrany jsou v příslušných
seznamech této třídy. Vrcholy a hrany jsou poté implementovány také jako třídy.

Každý vrchol má seznam hran, které z něho jdou a také seznam sousedů, kam vedou
zmíněné hrany.

Každá hrana je podtřída třídy :class:`~graph_catalog.graph.Edge` podle toho jaký
typ hrany reprezentuje. Dle podtřídy jsou také uloženy vrcholy, mezi kterými
hrana vede.