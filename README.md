# Web Scraping Car Components

In this repository, the website buycarparts.co.uk is scraped. 
If you wan to try the code yourself in your computer,
firs thing you should do is to install all dependencies.

You can do that from the terminal with the command: 
```
pip install -r requirements.txt
```

Before running the scraper, you should also navigate to 
a specific car, obtain the url set the path variable.
For instance, in the following situation, the scraper
wouldn't work: 

```
path = "https://www.buycarparts.co.uk/"
```

As I said previously, the script needs a specific car. 
In this case, the script would scrape the AUDI A6 C8
Allroad (4AH) 50 TDI Mild Hybrid quattro Diesel

```
path = "https://www.buycarparts.co.uk/audi/a6-allroad-4ah-c8/136391"
```


