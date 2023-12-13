Můj algoritmus vyplňuje plochu dílky ze hry Carcasonne.
Dílky jsem nalezla zde: https://wikicarpedia.com/car/Carcassonne_Tile_List/en.

Hrany dílků mohou být typu CITY, GRASS a PATH.
Algoritmus generuje plochu tak, aby hrany sousedních dílků odpovídaly, náhodně vybere dílek ze seznamu vhodných kandidátů.
Pokud dojde k situaci, že nelze umístit další dílek, algoritmus se vrací a mění umístění dříve umístěných dílků.
První dílek je vybrán náhodně, další pomocí algoritmu prohledávání do šířky.
Další podrobnosti jsou popsány v komentářích kódu.

