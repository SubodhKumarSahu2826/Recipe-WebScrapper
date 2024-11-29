import csv
import tkinter as tk
search_results_frame = None  
def load_recipes():
    recipes = []
    with open('recipes.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            recipes.append({
                'Recipe Name': row[0],
                'Ingredients': row[1],
                'Instructions': row[2]
            })
    return recipes
def search_recipes_by_name(recipes, query):
    results = []
    for recipe in recipes:
        if query.lower() in recipe['Recipe Name'].lower():
            results.append(recipe)
    return results
def display_recipe_in_gui(recipe):
    recipe_window = tk.Toplevel(root)
    recipe_window.title(recipe['Recipe Name'])


    recipe_name_label = tk.Label(recipe_window, text="Recipe Name: " + recipe['Recipe Name'], font=('Helvetica', 12, 'bold'), fg='black')
    recipe_name_label.pack(pady=(10, 5))


    ingredients_text = recipe['Ingredients'].replace('▢', '\n▢')
    ingredients_label = tk.Label(recipe_window, text="Ingredients:\n\n" + ingredients_text, font=('Helvetica', 15), wraplength=1500, justify="left")
    ingredients_label.pack(pady=(0, 10))


    instructions_text = recipe['Instructions'].replace('.', '\n')  
    instructions_label = tk.Label(recipe_window, text="Instructions:\n\n" + instructions_text, font=('Helvetica', 15), wraplength=1500, justify='left')
    instructions_label.pack(pady=(0, 10))
def search_recipe():
    global search_results_frame 
    query = search_entry.get()
    search_results = search_recipes_by_name(recipes, query)
    if len(search_results) == 0:
        search_results_label.config(text="No recipes found matching the given name.", fg='red')
    else:
        search_results_label.config(text="")
        if search_results_frame:
            search_results_frame.destroy() 
        search_results_frame = tk.Frame(root)
        search_results_frame.pack(pady=(10, 0))
        for i, recipe in enumerate(search_results):
            recipe_button = tk.Button(search_results_frame, text=recipe['Recipe Name'], font=('Helvetica', 10, 'bold'), command=lambda r=recipe: display_recipe_in_gui(r))
            recipe_button.grid(row=i, column=0, padx=10, pady=5, sticky='ew')
if __name__ == "__main__":
    recipes = load_recipes()
    root = tk.Tk()
    root.title("Baba ka Dhaba Recipe")
    root.geometry("600x400")
    title_label = tk.Label(root, text="Baba ka Dhaba Recipe", font=('Helvetica', 24, 'bold'), fg='black')
    title_label.pack(pady=(20, 10))
    subtitle_label = tk.Label(root, text="Enter your title", font=('Helvetica', 14, 'bold'), fg='black')
    subtitle_label.pack()
    search_frame = tk.Frame(root)
    search_frame.pack(pady=(10, 0))


    search_entry = tk.Entry(search_frame, font=('Helvetica', 12), width=40)
    search_entry.grid(row=0, column=0, padx=10, pady=5)


    search_button = tk.Button(search_frame, text="Search", font=('Helvetica', 12, 'bold'), command=search_recipe)
    search_button.grid(row=0, column=1, padx=10, pady=5)


    search_results_label = tk.Label(root, text="", font=('Helvetica', 12), fg='red')
    search_results_label.pack()


    root.mainloop() 