import { Card, CardContent, CardMedia, Typography } from "@mui/material";

const PokemonCard = ({ name, image, description }) => {
  return (
    <Card sx={{ maxWidth: 200, m: 1 }}>
      <CardMedia component="img" height="140" image={image} alt={name} />
      <CardContent>
        <Typography variant="h6">{name}</Typography>
        <Typography variant="body2" color="text.secondary">
          {description}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default PokemonCard;
