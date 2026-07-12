import { useEffect, useState } from "react";
import PokemonCard from "./components/PokemonCard";
import { Box, Typography } from "@mui/material";

function App() {
  const [pokemons, setPokemons] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPokemons = async () => {
      try {
        const res = await fetch("https://pokeapi.co/api/v2/pokemon?limit=30");
        const data = await res.json();

        const detailedData = await Promise.all(
          data.results.map(async (pokemon) => {
            const res = await fetch(pokemon.url);
            const details = await res.json();
            return {
              name: pokemon.name,
              image: details.sprites.front_default,
              description: `Height: ${details.height}, Weight: ${details.weight}`,
            };
          })
        );

        setPokemons(detailedData);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching Pokémon:", error);
      }
    };

    fetchPokemons();
  }, []);

  const sortedPokemons = pokemons.toSorted((a, b) =>
    a.name.localeCompare(b.name)
  );

  if (loading) return <Typography variant="h4">Cargando...</Typography>;

  return (
    <Box sx={{ display: "flex", p: 2 }}>
      {/* Lado izquierdo - sin ordenar */}
      <Box sx={{ flex: 1 }}>
        <Typography variant="h5">Sin ordenar</Typography>
        <Box sx={{ display: "flex", flexWrap: "wrap" }}>
          {pokemons.map((p) => (
            <PokemonCard key={p.name} {...p} />
          ))}
        </Box>
      </Box>

      {/* Lado derecho - ordenado */}
      <Box sx={{ flex: 1 }}>
        <Typography variant="h5">Ordenado (A-Z)</Typography>
        <Box sx={{ display: "flex", flexWrap: "wrap" }}>
          {sortedPokemons.map((p) => (
            <PokemonCard key={p.name} {...p} />
          ))}
        </Box>
      </Box>
    </Box>
  );
}

export default App;
