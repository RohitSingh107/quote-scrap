
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

# Function to scrape quotes
def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").get_text()
        # print(f"quote is {quote}------------------------------------------------------------------------------------------------------")

        # print(f"quote length is {len(quotes)}")
        author = quote.find("small", class_="author").get_text()
        print(f"author is {author}----------------------------------------------------------------------------")
        quotes.append({"text": text, "author": author})
    return quotes

# Route to display scraped quotes
@app.route("/")
def display_quotes():
    quotes = scrape_quotes()
    return render_template("index.html", quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)
