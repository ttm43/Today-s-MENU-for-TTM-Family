## Creating a Model to Decide What to Eat

1. **Define Dataset**: Start by gathering a diverse set of recipes. Include dish names, ingredients, preparation time, and dietary restrictions. The broader dataset, the more personalized suggestions can be.
2. **Determine Conditions for Suggestions**: Consider factors like:

   - Time of day (breakfast, lunch, dinner)
   - Dietary preferences (vegetarian, low-carb)
   - Available ingredients
   - Desired cooking time
   - Nutritional goals

   These conditions help tailor suggestions to individual needs.
3. **Create the Suggestion Algorithm**: Start with a simple algorithm that selects dishes randomly based on set conditions. Evolve this to include user preferences, nutritional balance, and shopping list generation.
4. **Implement and Iterate**: Build model as a script or app. Test extensively to refine its performance. Use early user feedback to make improvements.
5. **Expand and Enhance**: Add features like nutritional analysis, user rating systems, and grocery shopping integrations. Continually update model based on feedback and new insights.

## Code modificaiton history

* 13/03/2024  create base edition recommand script, which will generate 2 dishes without similar main ingredients, however, it was noticed that this approach might recommend two dishes with similar flavors. Therefore, in the next update, each dish will be assigned a flavor attribute. The cosine similarity between them will be calculated, and a threshold will be set. If the similarity exceeds this threshold, it will be considered that the (flavors, cooking method and so on) of the two dishes are similar, and they won't be recommended repeatedly.
