import bands_list_scraper
import collector
import status_analysis


def main():
    bands_list_scraper.scrape_band_list()
    collector.collect_and_store_band_data()
    status_analysis.draw_all()


if __name__ == '__main__':
    main()
