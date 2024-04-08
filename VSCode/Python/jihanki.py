def jihanki():
    print("お金を入れてください")
    okane = int(input())

    if okane == 1 or okane == 5 or okane == 10 or okane == 50 or okane == 100 or okane == 1000:
        print( "投入金額は" + str(okane) + "円です" )
    elif okane == 5000 or okane == 10000:
        print( "投入された紙幣は使用できません" )
    else:
        print( str(okane) + "円なんてない！" )

jihanki()