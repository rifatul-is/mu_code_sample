# mu_code_sample
The program manages a dictionary of terms and their descriptions stored in a JSON file, allowing users to perform CRUD (Create, Read, Update, Delete) operations on the data. 
1. The program starts by loading data from data.json into the data dictionary and asks the user for the following input to proceed.
  - **Exit**: Entering **'0'** exits the program.
  - **Help**: Entering **'1'** displays all current keys from the json file.
  - **Add/Update**: By Entering **'2'**, users can add a term or update an existing one.
  - **Delete**: Entering **'3'** allows users to delete a term.
  - **Term Search**: Any other input is treated as a term to search for its description or displays similar terms if the term is not found.
2. **Loading and Saving Data**: The `load_data(file_path)` and `save_data(file_path, data)` handle reading from and writing to the JSON file, ensuring data is saved across sessions.
3. **Adding and Deleting Terms**: The `add_or_update_term(term, description, data)` adds a new term or updates an existing term with a new description if it already exists in the dictionary. The `delete_term(term, data)` removes a term from the dictionary if it exists.
4. **Search and Suggestions**: The `get_info(term, data)` function searches for exact matches of terms in the dictionary. If a term is not found, `get_similar_terms(term, data)` provides suggestions by listing terms that contain the term as a substring.
