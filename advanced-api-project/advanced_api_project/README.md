# Advanced API Project

## API Endpoints

### List Books
- **URL**: `/api/books/`
- **Method**: `GET`
- **Description**: Retrieve a list of all books.

### Create Book
- **URL**: `/api/books/create/`
- **Method**: `POST`
- **Description**: Add a new book. Requires authentication.

### Update Book
- **URL**: `/api/books/update/<id>/`
- **Method**: `PUT`
- **Description**: Update an existing book. Requires authentication.

### Delete Book
- **URL**: `/api/books/delete/<id>/`
- **Method**: `DELETE`
- **Description**: Remove a book. Requires authentication.
## API Features

### Filtering
- **Filter by Title**: `/api/books/?title=Book Title`
- **Filter by Author**: `/api/books/?author=Author Name`
- **Filter by Publication Year**: `/api/books/?publication_year=2023`

### Searching
- **Search by Title or Author**: `/api/books/?search=Some Text`

### Ordering
- **Order by Title**: `/api/books/?ordering=title`
- **Order by Publication Year**: `/api/books/?ordering=publication_year`