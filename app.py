from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

app = Flask(__name__)


# Route to the Home Page
@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def home():
    """
    This is the route for the home/base page
    :return: Renders the index.html template
    """
    return render_template('index.html')


# Route to show the Result Reviews on result.html
@app.route('/review', methods=['GET', 'POST'])
@cross_origin()
def review():
    """
    This is the route to the result.html.

    In this function, we find the reviews of the first searched result
    based on the searched query passed.

    Searching is done by getting the source code of the page
    then parsing it using Beautiful Soup
    and accessing the tags and classes of the html elements

    Then only one search result is selected
    and all the comment boxes present on that page is selected
    and all the details are extracted in the form of dictionary and stored in the list.
    :return: Renders the result.html if everything goes fine. Otherwise returns index.html
    """

    if (request.method == 'POST'):

        try:
            search_str = request.form['content'].replace(" ", "")
            flipkart_base_url = "https://flipkart.com"

            # Searching for the product on Flipkart
            flipkart_url = "https://flipkart.com/search?q=" + search_str
            uClient = urlopen(flipkart_url)
            flipkart_page = uClient.read()
            uClient.close()

            # Parsing the Flipkart page
            flipkart_html = bs(flipkart_page, "html.parser")

            # Getting the html details of the searched result
            products = flipkart_html.find_all("div", {"class": "_1AtVbE col-12-12"})
            del products[0:3]

            # Selecting the first searched product
            first_product = products[0]

            # Opening the first searched product's details page using a href
            first_product_url = "https://flipkart.com" + first_product.div.div.div.a['href']
            first_product_page = requests.get(first_product_url)
            first_product_page.encoding = "utf-8"
            first_product_html = bs(first_product_page.text, "html.parser")

            # Gathering the html details for the comment boxes
            comment_boxes = first_product_html.find_all("div", {"class": "_16PBlm"})

            # Creating a csv file to store the reviews
            filename = search_str + ".csv"
            file = open(filename, 'w')
            columns = "Product, Customer Name, Rating, Comment Heading, Comment \n"
            file.write(columns)

            reviews_list = []

            for comment in comment_boxes:

                # Gathering Name of the Person
                try:
                    name = comment.div.div.find_all("p", {"class": '_2sc7ZR _2V5EHH'})[0].text

                except:
                    name = "No Name"

                # Gathering Ratings of the person
                try:
                    ratings = comment.div.div.div.div.text

                except:
                    ratings = "No Ratings"

                # Gathering the Heading of the Comment
                try:
                    heading = comment.div.div.div.p.text

                except:
                    heading = "No Comment Heading"

                # Gathering the Comment of the Person
                try:
                    comment_tag = comment.div.div.find_all('div', {'class': ''})
                    cust_comment = comment_tag[0].div.text

                except Exception as e:
                    print(f"Exception while gathering the comment: {e}")

                review_dict = {"Product": search_str, "Customer Name": name, "Rating": ratings,
                               "Comment Heading": heading, "Comment": cust_comment}
                reviews_list.append(review_dict)

            return render_template("result.html", reviews=reviews_list[:(len(reviews_list) - 1)])

        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something Went Wrong'

    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
