import React from 'react';
import { Heart } from 'lucide-react';
import RecipeCard from './RecipeCard';

const RecipeGrid = ({ recipes, onSelectRecipe }) => {
  if (recipes.length === 0) {
    return (
      <div className="empty-state">
        <Heart size={64} style={{ color: 'var(--color-primario)' }} />
        <h3>No encontré respuestas</h3>
        <p>Intenta ajustar tu búsqueda o filtros</p>
      </div>
    );
  }

  return (
    <div className="recipe-grid">
      {recipes.map(recipe => (
        <RecipeCard 
          key={recipe.id} 
          recipe={recipe} 
          onClick={onSelectRecipe} 
        />
      ))}
    </div>
  );
};

export default React.memo(RecipeGrid);
