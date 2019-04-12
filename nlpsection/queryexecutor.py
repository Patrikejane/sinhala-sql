
from queryGenarate import genarate_query
from sqlexcetor import get_connection,close_connection

# strLine = " සිසුන්ගේ නම ලකුණු දෙන්න "
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ක් ලබාගත් "
# strLine = " ලකුණු 75 ට සමාන සහ වයස 22 ට සමාන සිසුන්ගේ නම දෙන්න "
strLine = " සිසුන්ගේ නම ලකුණු කුමක්ද ලකුණු 75 ට වැඩි "
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22 ට සමාන සමාන සමාන සමාන "
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස වයස 22 ට සමාන "
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22 සමාන "
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22 "
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22 ට සමාන "
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සමාන සමාන සහ වයස 22 ට සමාන "
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22 ට සමාන සහ "
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ සහ වයස 22 ට සමාන "
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22 සමාන "

# strLine = " සිසුන්ගේ උපරිම ලකුණු ලබාදෙන්න "
# strLine = " වයස 21 ට සමාන සිසුන්ගේ අවම ලකුණු කුමක්ද "
# strLine = " සිසුන්ගේ නම ලබාදෙන්න ලකුණු අනුපිලිවලින් "
# strLine = " සිසුන්ගේ නම ලබාදෙන්න ලකුණු පිලිවලින් "
# strLine = " ලකුණු අනුපිලිවලින් සිසුන්ගේ නම ලබාදෙන්න "
# strLine = " සිසුන්ගේ ලකුණු වල සාමාන්යය දෙන්න "
# strLine = " වයස 21 ට වැඩි සිසුන්ගේ ලකුණු වල සාමාන්යය දෙන්න "
# strLine = " සිසුන්ගේ ලකුණු වල එකතුව දෙන්න "
# strLine = " වයස 21 ට වැඩි සිසුන්ගේ වල එකතුව දෙන්න "
# strLine = " සිසුන් කොපමණ සිටීද "
# strLine = " සිසුන් ගණන කීයද "
# strLine = " සියලු සිසුන් ප්රමාණය දෙන්න "
# strLine = " වයස 21 ට වැඩි සිසුන් කොපමණ සිටීද "

#
# GENARATED_SQL_QUERY = genarate_query(strLine)
# print("----------- Genarated Query -----------" )
# print("genarated query : " + '[ ' + GENARATED_SQL_QUERY + ']')
#
#
# user, password, host, database = 'root', 'sunimalroot', '127.0.0.1', 'nlpDb'
#
#
# connection = get_connection(user, password, host, database)
#
# cursor = connection.cursor()
# cursor.execute(GENARATED_SQL_QUERY)
#
# print("----------- query Results -----------" )
# for i in cursor:
#     print(i)
#
# print("----------- query Results -----------" )
# close_connection(cursor)


def execute_query(strLine):
    GENARATED_SQL_QUERY = genarate_query(strLine)
    print("----------- Genarated Query -----------")
    print("genarated query : " + '[ ' + GENARATED_SQL_QUERY + ']')

    user, password, host, database = 'root', 'sunimalroot', '127.0.0.1', 'nlpDb'

    connection = get_connection(user, password, host, database)

    cursor = connection.cursor()
    cursor.execute(GENARATED_SQL_QUERY)

    print("----------- query Results -----------")
    results = []
    for i in cursor:
        print(i)
        results.append(i)

    print("----------- query Results -----------")
    close_connection(cursor)

    return results