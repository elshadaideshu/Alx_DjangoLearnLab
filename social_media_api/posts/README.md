## API Endpoints

### Posts

- **Create Post**
  - **POST** `/api/posts/`
  - **Request Body**:
    ```json
    {
      "title": "My First Post",
      "content": "This is the content of the post."
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "author": 1,
      "title": "My First Post",
      "content": "This is the content of the post.",
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
    ```

- **List Posts**
  - **GET** `/api/posts/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "author": 1,
        "title": "My First Post",
        "content": "This is the content of the post.",
        "created_at": "2023-01-01T00:00:00Z",
        "updated_at": "2023-01-01T00:00:00Z"
      }
    ]
    ```

### Comments

- **Create Comment**
  - **POST** `/api/comments/`
  - **Request Body**:
    ```json
    {
      "post": 1,
      "content": "This is a comment."
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "post": 1,
      "author": 1,
      "content": "This is a comment.",
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
    ```