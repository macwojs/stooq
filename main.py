import stooq_today_news as stooq

if __name__ == '__main__':
    print("\n\n*****************  WIG 20 *****************")
    stooq.print_today_news(stooq.tick_WIG20)
    print("\n\n***************** mWIG 40 *****************")
    stooq.print_today_news(stooq.tick_mWIG40)
    print("\n\n***************** sWIG 80 *****************")
    stooq.print_today_news(stooq.tick_sWIG80)

