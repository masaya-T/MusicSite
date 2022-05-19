from mutagen.easyid3 import EasyID3
import glob
import pandas as pd
import  sqlite3

music_df=pd.DataFrame(
    columns =['id','album', 'title', 'artist', 'tracknumber','genre','date','path']
    )
def get_mp3_info(mp3_file_path):
    global music_df
    
    tags = EasyID3(mp3_file_path)
    if '(' in tags['title']:
        return 
    # 辞書型で格納されたメタデータを注出
    data={'id':'','album':'', 'title':'', 'artist':'', 'tracknumber':'','genre':'','date':'','path':''}
    data['id']= len(music_df)
    for key, value in tags.items():
        data[key]= value[0]
    
    data['path']=mp3_file_path
    s = pd.Series(list(data.values()), index=data.keys())
    music_df=music_df.append(s,ignore_index=True,sort=False)
    print(data)

        
def search_path(base_path):
    for path in glob.glob(base_path+'/**/*.mp3', recursive=True):
        print(path)
        get_mp3_info(path)
    print(music_df)

if __name__=='__main__':
    base_path='/mnt/NAS/music'
    search_path(base_path)
    #  データベースの作成
    file_sqlite3 = './music_info.db'
    conn = sqlite3.connect(file_sqlite3)
    music_df.to_sql('music_info',conn,if_exists='replace')
    conn.close()