## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SameerSahu007/Birdvision.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd birdvision
   ```
3. **Create and activate a virtual environment (Optional but recommended):**

   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   # For Windows
   venv\Scripts\activate
   # For macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```


## Running the Application

**Run the Flask application:**
```bash
    flask run
```
**Access the application in your web browser at `http://127.0.0.1:5000`.**

## Testing
 **Run tests:**
   ```bash
   pytest
   ```

## Endpoints

### 1. Get All Products

- **URL:** `/products`
- **Method:** GET
- **Description:** Retrieve a list of all products.

### 2. Get Product by ID

- **URL:** `/products/<id>`
- **Method:** GET
- **Description:** Retrieve details of a product by its ID.

### 3. Add New Product

- **URL:** `/products`
- **Method:** POST
- **Description:** Add a new product.

### 4. Update Product

- **URL:** `/products/<id>`
- **Method:** PUT
- **Description:** Update details of an existing product by its ID.

### 5. Delete Product

- **URL:** `/products/<id>`
- **Method:** DELETE
- **Description:** Delete a product by its ID.
