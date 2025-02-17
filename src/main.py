def main():
    from scraper import Scraper

    # Initialize the scraper
    crypto_scraper = Scraper()

    # Fetch cryptocurrency data
    data = crypto_scraper.fetch_data()

    # Parse the fetched data
    parsed_data = crypto_scraper.parse_data(data)

    # Print or save the parsed data
    print(parsed_data)

if __name__ == "__main__":
    main()