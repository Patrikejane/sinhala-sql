
from sklearn.externals import joblib



# model = {'මිනිස්සුන්': 'T','කුරුල්ලන්':'T','ගස':'Attr','ලගින':'O','කපන':'O'}
sqlMapper_dict = {}
with open('meta_data_post_process.csv') as post_p_file:

    headerline = post_p_file.readline()
    for i in post_p_file:
        singleline = i.rstrip("\n").split(',')
        if len(singleline) == 4 :
            sqlMapper_dict[singleline[1]] = singleline[2]
        else:
            print("Invalid row : ", singleline)


joblib.dump(sqlMapper_dict, 'sqlMapper.pkl')


