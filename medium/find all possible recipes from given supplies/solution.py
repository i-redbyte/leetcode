from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe_to_ingredients = {recipe: set(ingr) for recipe, ingr in zip(recipes, ingredients)}
        available_supplies = set(supplies)
        result: List[str] = []
        recipes_to_check = set(recipes)

        def can_cook(recipe: str) -> bool:
            for ingredient in recipe_to_ingredients[recipe]:
                if ingredient not in available_supplies:
                    return False
            return True

        while recipes_to_check:
            removable_recipes = []

            for recipe in recipes_to_check:
                if can_cook(recipe):
                    result.append(recipe)
                    available_supplies.add(recipe)
                    removable_recipes.append(recipe)

            for recipe in removable_recipes:
                recipes_to_check.remove(recipe)

            if not removable_recipes:
                break

        return result


s = Solution()
print(s.findAllRecipes(recipes=["bread"], ingredients=[["yeast", "flour"]], supplies=["yeast", "flour", "corn"]))
print(s.findAllRecipes(recipes=["bread", "sandwich"], ingredients=[["yeast", "flour"], ["bread", "meat"]],
                       supplies=["yeast", "flour", "meat"]))
print(s.findAllRecipes(recipes=["bread", "sandwich", "burger"],
                       ingredients=[["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                       supplies=["yeast", "flour", "meat"]))
