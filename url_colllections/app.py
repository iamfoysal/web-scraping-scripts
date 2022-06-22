from scrap import wlog
from scrap import wscrap



wlog.log_info('html/error.log')
scrap = wscrap.AmazonScraper(wscrap.url_az, wlog)
scrap.retrive_webpage()
scrap.write_web_page()
scrap.read_web_page()
scrap.convate_to_soup()
scrap.print_data()
scrap.parseSope_to_html()