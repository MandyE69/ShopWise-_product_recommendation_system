from flask import Flask, request, render_template
import pandas as pd
import random
from flask_sqlalchemy import SQLAlchemy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# load files===========================================================================================================
trending_products = pd.read_csv("models/trending_product.csv")
train_data = pd.read_csv("models/clean_data1.csv")
# popular=pd.read_pickle('models/popular.pkl')


# Recommendations functions============================================================================================
# Function to truncate product name
def truncate(text, length):
    if len(text) > length:
        return text[:length] + "..."
    else:
        return text


def content_based_recommendations(train_data, item_name, top_n=10):
    # Check if the item name exists in the training data
    if item_name not in train_data['Name'].values:
        print(f"Item '{item_name}' not found in the training data.")
        return pd.DataFrame()

    # Create a TF-IDF vectorizer for item descriptions
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    # Apply TF-IDF vectorization to item descriptions
    tfidf_matrix_content = tfidf_vectorizer.fit_transform(train_data['Tags'])

    # Calculate cosine similarity between items based on descriptions
    cosine_similarities_content = cosine_similarity(tfidf_matrix_content, tfidf_matrix_content)

    # Find the index of the item
    item_index = train_data[train_data['Name'] == item_name].index[0]

    # Get the cosine similarity scores for the item
    similar_items = list(enumerate(cosine_similarities_content[item_index]))

    # Sort similar items by similarity score in descending order
    similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)

    # Get the top N most similar items (excluding the item itself)
    top_similar_items = similar_items[1:top_n+1]

    # Get the indices of the top similar items
    recommended_item_indices = [x[0] for x in top_similar_items]

    # Get the details of the top similar items
    # recommended_items_details = train_data.iloc[recommended_item_indices][['Name', 'ReviewCount', 'Brand', 'ImageURL', 'Rating']]
   
    recommended_items_details = train_data.iloc[recommended_item_indices][['Name', 'ReviewCount', 'Brand', 'ImageURL', 'Rating', 'Price']]

    return recommended_items_details

   
# routes===============================================================================

@app.route("/")
def index():   
    product_image_urls = list(trending_products['ImageURL'].values)
    
    # price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
    price = list(train_data['Price'].values)
    return render_template('index.html',trending_products=trending_products.head(8),truncate = truncate,
                           random_product_image_urls=product_image_urls,
                           price = price
    )


@app.route("/main")
def main():
    # Default value for content_based_rec

     # Get a unique list of product names from the dataset
    product_list = train_data['Name'].dropna().unique()
    product_list = sorted([product for product in product_list if product[0].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])

    # Limit the product list to 1,000 items
    product_list = product_list[:1000]

    content_based_rec = pd.DataFrame()
    message1 = "Welcome! Please search for product recommendations."
    return render_template('main.html', content_based_rec= content_based_rec, message=message1, product_list= product_list, truncate = truncate)


# routes
@app.route("/index")
def indexredirect():
    # Create a list of random image URLs for each product
    # random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
    random_product_image_urls = list(trending_products['ImageURL'].values)
    # price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
    price = list(train_data['Price'].values)
    return render_template('index.html', trending_products=trending_products.head(8), truncate=truncate,
                           random_product_image_urls=random_product_image_urls,
                        #    random_price=random.choice(price))
                        price = price
    )


@app.route("/recommendations", methods=['POST', 'GET'])
def recommendations():
    product_list = train_data['Name'].dropna().unique()
    product_list = sorted([product for product in product_list if product[0].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
    # Limit the product list to 1,000 items
    product_list = product_list[:1000]

    content_based_rec = None  # Initialize as None for all requests
    message = None  # Default message
    random_product_image_urls = []  # Default empty image URLs
    price = []  # Default empty prices

    if request.method == 'POST':    
        prod = request.form.get('prod')
        
        # Print the input product name to debug
        print("Product received:", prod)

        # Validate and process the 'nbr' input
        nbr_value = request.form.get('nbr')  # Retrieve the form value
        if nbr_value and nbr_value.isdigit():
            nbr = int(nbr_value)  # Convert to integer if valid
        else:
            nbr = 0  # Default to 0 if invalid or empty

        print("Number of recommendations:", nbr)

        # Generate recommendations
        content_based_rec = content_based_recommendations(train_data, prod, top_n=nbr)

        # Check if recommendations are empty
        if content_based_rec.empty:
            message = "Please select a product to get recommend."
        else:
            message = "Here are the recommended products:"

            # Generate image URLs 
          
            random_product_image_urls = list(train_data['ImageURL'].values)
            price = list(train_data['Price'].values)
            

    return render_template(
        "main.html",
        content_based_rec=content_based_rec,
        truncate=truncate,
        message=message,
        random_product_image_urls=random_product_image_urls,
        price =price,
        # random_price = random.randint(20, 200),
        product_list = product_list 
        
    )
    
    return render_template("main.html")



if __name__=='__main__':
    app.run(debug=True)
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)