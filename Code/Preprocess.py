import pandas as pd
import os
import json

def processing_data(file_path):
    
    # Extract the file name without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    # Extract the year from the file name
    year = file_name.split('_')[1]
    disaster = file_name.split('_')[0]

    df=pd.read_excel(file_path)
    # Drop column "Unnamed: 0"
    df.drop("Unnamed: 0", axis=1, inplace=True)

    #Drop column ga perlu dan jadikan Index column berdasarkan row 3
    df.columns = df.iloc[3]
    df = df.drop([0,1,2,3,4], axis=0)

    #Reset COlumn Index
    df = df.reset_index(drop=True)
    # change column names
    df.columns = ['Wilayah', 'Jumlah', 'Meninggal', 'Hilang', 'Terluka', 'Menderita', 'Mengungsi', 'Rumah', 'Pendidikan', 'Kesehatan', 'Peribadatan', 'Fasum', 'Perkantoran', 'Jembatan', 'Pabrik', 'Kios']

    #Drop column yang ada di row terakhir
    to_drop = ["Bidang Pengelolaan Data dan Sistem Informasi (PDSI),",
            "Pusat Data Informasi dan Komunikasi Kebencanaan (Pusdatinkom),",
            "Badan Nasional Penanggulangan Bencana (BNPB)",
            "Jumlah"]
    df = df[~df.iloc[:,0].isin(to_drop)]

    # Menghilangkan angka pada kolom wilayah
    df['Wilayah'] = df['Wilayah'].apply(lambda x: x[x.find('. ')+2:])

    # Menambahkan kolom Jenis Bencana dan Tahun Terjadinya Bencana
    df['Jenis Bencana'] = disaster
    df['Tahun'] = year
    df['id'] = df[['Wilayah', 'Jenis Bencana','Tahun']].sum(axis=1).map(hash)
    df.fillna(0,inplace=True)
    
    json_data=df.to_json(f"E:/tugas_koko/Mencari_Kerja/Kerjaan/Paw_Patrol/Development/Data/{disaster}_{year}.json",orient="records",indent=4)
    # filename = f"E:/tugas_koko/Mencari_Kerja/Kerjaan/Paw_Patrol/Development/Data/{disaster}_{year}.json"
    # with open(filename, 'w', encoding='utf-8') as f:
    #     json.dump(json_data, f, ensure_ascii=False, indent=4)

    # return df

    
    return json_data,df

