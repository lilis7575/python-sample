


def exchage_money(exchage_to, krw) :

    rates = [('usd', 1196.50), ('jpy', 10.2629), ('eur', 1262.85), ('cny', 175.06)]

    for rate in rates :
        if exchage_to == rate[0]:
            amount = krw / rate[1]
            print(exchage_to.upper() + " 환율은 " + format(rate[1], '.2f') + " 입니다.")
            print(str(krw) + " KRW를 환전한 결과는 " + format(amount, ".2f") + " " + exchage_to.upper() + " 입니다.")
            print()

            break
    return


exchage_money('usd', 100000)
exchage_money('jpy', 100000)
exchage_money('eur', 100000)
exchage_money('cny', 100000)
