



# Personal Blog API

Project from :https://roadmap.sh/projects/personal-blog

This project is a personal blog API where users can view articles as guests, and the admin can add, edit, or delete articles. Articles are stored in the `articles.json` file in JSON format.

## Features

### Guest Section
- **Home Page**: Displays a list of all published articles.
- **Article Page**: Displays the details of a specific article, including the title, content, and publication date.

### Admin Section
- **Dashboard**: Displays a list of all published articles with options to add, edit, or delete an article.
- **Add Article**: Allows the admin to add a new article.
- **Edit Article**: Allows the admin to edit an existing article.
- **Delete Article**: Allows the admin to delete an article.

## Installation and Running the Project

1. **Requirements**
   - Python 3.x
   - Flask (Install via: `pip install flask`)

2. **File Structure**
   - `personalblog.py`: Main application file for the Flask API.
   - `articles.json`: Data file where articles are stored.

3. **Running the Application**
   ```bash
   python personalblog.py

