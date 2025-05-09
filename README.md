# ShopWise: Product Recommendation System in ML

ShopWise is a machine learning-based product recommendation system designed to enhance the shopping experience by suggesting relevant products based on user input. It leverages content-based filtering techniques to provide personalized recommendations. The application is built with Flask for the backend, Jinja2 for templating, and Bootstrap for responsive design.

---

## Features

- **Dynamic Product Recommendations**: Provides tailored recommendations based on the selected product.
- **Interactive User Interface**:
  - Search bar for product selection and custom number of recommendations.
  - Responsive card layout to display product details.
  - Modal pop-ups for viewing detailed product information.
- **Customizable Experience**:
  - Theme selection (Default, Black, Green).
  - Zoom functionality for accessibility.
- **Responsive Design**: Mobile-friendly layout using Bootstrap.

---

## Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, Bootstrap, Jinja2
- **Storage**: Dataset for product data
- **Machine Learning**: Content-based recommendation system, Popularity-based filtering
- **Deployment**: Compatible with local or cloud-based deployments (e.g., Heroku)

---

## Project Structure

ShopWise/ │ 
├── models/ 
   │ ├── clean_data1.csv #train data
   │ ├── trending_products.csv #dataset for trending product
├── static/
  │ ├── css/ # Additional CSS files
  │ ├── js/ # JavaScript files 
  │ └── images/ # Product images and assets 
├── templates/ 
  │ ├── index.html # Main recommendation page 
  │ └── main.html # Base template (if applicable) 
├── app.py # Flask application 
├── requirements.txt # Required Python packages 
└── README.md # Project documentation


---

## Installation

  Follow these steps to set up the project locally:
  
  1. **Clone the repository**:
       ```bash
       git clone https://github.com/yourusername/ShopWise.git
       cd ShopWise
  
  2. **Create a virtual environment**:
  
      ```bash
        python3 -m venv venv
        source venv/bin/activate # For Linux/Mac
        venv\Scripts\activate    # For Windows
  
  3. **Install dependencies**:
  
      ```bash
          pip install -r requirements.txt
  
  4. **Run the application**:
      ```bash
        python app.py
      
  5. **Access the app: Open your browser and navigate to http://127.0.0.1:5000.**

## Usage:
  1. Trending product on homepage
  2. Select a product from the dropdown menu on the recommendation.
  3. Enter the number of recommendations you want to view.
  4. Click the "Search" button to generate recommendations.
  5. Browse through the recommended products and view their details in modal pop-ups.

## Screenshots
  **Home Page**
    ![Screenshot (141)](https://github.com/user-attachments/assets/4fb7ec0d-67eb-4c31-8816-5d70bf8e4a5a)

  **Recommended Products**
    ![Screenshot (144)](https://github.com/user-attachments/assets/85da7bdf-653b-47b3-98bc-f67ead67ea1b)

## Future Enhancements
  1. Add collaborative filtering to improve recommendations.
  2. Integrate user authentication and personalization.
  3. Use a database (e.g., MySQL or MongoDB) for better scalability.
  4. Add a cart feature to save recommended products.
  5. Deploy the application to a cloud platform (e.g., AWS, Heroku).

## Contributing
  Contributions are welcome! Please follow these steps to contribute:

**Fork the repository.**
1. Create a feature branch:
    ```bash
        Copy code
        git checkout -b feature/your-feature-name
2. Commit your changes:
      ```bash
        Copy code
        git commit -m "Add your message here"
3. Push to the branch:
    ```bash
      Copy code
      git push origin feature/your-feature-name
 4. Open a pull request.


## Acknowledgments
  Bootstrap: For providing responsive UI components.
  Flask: For powering the backend of the application.
  Font Awesome: For icons used in the UI.

Contact
For any queries or suggestions, feel free to reach out:

  Email: madhavgyawali436@gmail.com
  GitHub: MandyE69

## Star 🌟 the repository if you find it helpful!




