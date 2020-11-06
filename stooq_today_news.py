from bs4 import BeautifulSoup
import requests
from datetime import datetime

def parse_date(date):
	date = date.text.strip().split('-')[0].strip()
	date = date.split(", ")
	if len(date[0])  == 5 :
		date[0] = '0'+date[0]
	date[0] = date[0][0:3]+month[date[0][3:]]+" "+str(datetime.now().year)
	if len(date[1])  == 4 :
		date[1] = '0'+date[1]
	date = date[0]+", "+date[1]
	# print(date)
	datetime_object = datetime.strptime(date, '%d %b %Y, %H:%M')

	return datetime_object

def get_page(tick):
	url = "https://stooq.pl/q/n/?s="+tick
	html_content = requests.get(url)
	html_content = html_content.content
	soup = BeautifulSoup(html_content.decode('utf-8','ignore'), "html.parser")
	return soup

def get_news(web_page):
	news_table=web_page.find("tbody", attrs={"valign": "top"})
	if news_table is not None:
		return news_table
	else:
		return -1

def get_news_title(news_table):
	news = news_table.find_all("font", attrs={"id": "f14"})
	news_array = []
	for new in news:
		news_array.append(new.find('a').text+"\t"+"https://stooq.pl/"+new.find('a')['href'])
	return news_array

def get_news_date(news_table):
	dates = news_table.find_all("font", attrs={"id": "a"})
	dates_array = []
	for date in dates:
		dates_array.append(parse_date(date))
	return dates_array

def print_today_news(tickets):
	today = datetime.today().date()
	for tick in tick_sWIG80:
		page = get_page(tick)
		news_page = get_news(page)
		if news_page != -1:
			news = get_news_title(news_page)
			dates = get_news_date(news_page)
			if dates[0].date() == today:
				print("\n\n***", tick, "***\n")
			for i in range(0, len(news)):
				if dates[i].date() == today:
					print(dates[i].time(), news[i])

month = {
    "sty" : 'Jan',
    "lut" : 'Feb',
    "mar" : 'Mar',
    "kwi" : 'Apr',
    "maj" : 'May',
    "cze" : 'Jun',
    "lip" : 'Jul',
    "sie" : 'Aug',
    "wrz" : 'Sep',
    "paź" : 'Oct',
    "lis" : 'Nov',
    "gru" : 'Dec'
    }

tick_sWIG80 = ["ABE", "ACG", "AGO", "AWM", "AML", "AMB", "APT", "ARH", "ATC", "ASB", "ABS", "AST", "1AT", "ATG", "APR", "BIO", "LWB", "BBT", "BRS", "BOS", "CIG", "CMP", "CRM", "CPG", "DBC", "EEX", "ENT", "FRO", "FTE", "GTN", "GNB", "GLC", "GRN", "HRP", "IDA", "INC", "IRL", "KGN", "KSW", "LTX", "LBW", "MCI", "MDG", "MNC", "MRB", "MLG", "MLS", "NET", "NWG", "OAT", "OPN", "BKM", "PCR", "PBX", "PEP", "PSW", "PHN", "PCE", "PXM", "R22", "RBW", "RVU", "SNK", "SLV", "SKA", "STX", "STP", "TIM", "TOR", "TOA", "TRK", "ULG", "UNT", "VGO", "VOX", "VRG", "WWL", "WLT", "WSE", "ZEP"]
tick_mWIG40 = ["11B", "AMC", "EAT", "ACP", "ASE", "BFT", "BML", "BNP", "BDX", "CIE", "CLN", "CMR", "DAT", "DVL", "DOM", "ECH", "ENA", "ENG", "EUR", "FMF", "GPW", "ATT", "GTC", "BHW", "ING", "CAR", "KER", "KTY", "KRU", "LVC", "MAB", "MBK", "MRC", "MIL", "NEU", "PKP", "PLW", "TEN", "WPL", "XTB"]
tick_WIG20	= ["ALR", "ALE", "CCC", "CDR", "CPS", "DNP", "JSW", "KGH", "LTS", "LPP", "OPL", "PEO", "PGE", "PGN", "PKN", "PKO", "PLY", "PZU", "SPL", "TPE"]


