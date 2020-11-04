# -*- coding: utf-8 -*-
"""
Here we check, how many companies are not included in the databases Academia_by_Country.sqlite and Industry.sqlite

"""
# from fuzzywuzzy import fuzz
import sqlite3
import time
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from varname import Wrapper
import nltk
import re
# Count average length of the titles (symbols and words) for:
# SEG and SPE conferences and SPE Journals
# SEG: 1982 - 2020
# SPE: 1980 - 2020
# Total 1980 - 2020
# Here we check the statistics for each of corresponding societies:
# 1) Number of journal papers 
# 2) Number of conference papers
# 3) Number of authors per year
def societies():
    
    conn = sqlite3.connect('onepetro_metadata.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT Society FROM Metadata")
    data_aca=cursor.fetchall()
    fontsize_det = 13
    Society_list = []
    
    for element in data_aca:
        
        if element[0] in Society_list:
            pass
        else: 
            Society_list.append(element[0])
    
    Society_list.sort()
        
    for soc in Society_list:
        print(soc)
        
    cursor = conn.cursor()
    cursor.execute("Select Title From Metadata Where (Society = 'SPE' and Year = '2019' )")
                
    
    list_lines = []
    data_aca=cursor.fetchall()
    fontsize_det = 13
    Society_list = []
    spe_string = ''
    for element in data_aca:
        spe_string = spe_string + element[0] + '\r\n'
        # list_lines.append(element[0])
    spe_string = spe_string.lower()
    spe_string = re.sub('( a | an | and | the | is | of | for )', '', spe_string)  
    
    
    
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    # tokens = nltk.word_tokenize(spe_string)
    tokens = tokenizer.tokenize(spe_string)

#Create your bigrams
    bgs = nltk.bigrams(tokens)
    
    #compute frequency distribution for all the bigrams in the text
    fdist = nltk.FreqDist(bgs)
    print(type(fdist))
    
    for element in fdist.most_common(10):
        for item in element[0]: print(item, end = ' ')
        print(element[1])
        

      
    # Loop through each line of the file 
    # for line in list_lines: 
        
    #     words = line.split(" ") 
      
    #     # Iterate over each word in line 
    #     for word in words: 
    #         # Check if the word is already in dictionary 
    #         if word in d: 
    #             # Increment count of word by 1 
    #             d[word] = d[word] + 1
    #         else: 
    #             # Add the word to dictionary with count 1 
    #             d[word] = 1
      
    # # Print the contents of dictionary 
    # for key in list(d.keys()): 
    #     print(key, ":", d[key]) 
        
    
    
    # print(spe_string)
    
    #     Total[element[0]].append(element[3])
    # count=0
    # slovary = [SPE_Conference, All_Conferences,  Total, SEG_Conferences, All_Journals, SPE_Journals]
    # types = ['SPE Conferences', 'All Conferences', 'Total', 'SEG Conferences',  'All Journals',  'SPE Journals']
    # dict_for_print_w = {}
    # dict_for_print_s = {}
    # for numbs in range(1980, 2021):
    #     dict_for_print_w[str(numbs)] = []
    #     dict_for_print_s[str(numbs)] = []
        
    # for slovar in slovary:
    #     for key, value in slovar.items():
    #         sum_words = 0
    #         sum_symbs = 0
    #         if value == []:
    #             pass
    #         else:
    #             for titles in value:
    #                 sum_words = sum_words + titles.count(' ') + 1
    #                 sum_symbs = sum_symbs + len(titles)
    #         try:    
    #             dict_for_print_w[key].append(sum_words/len(value))
    #             dict_for_print_s[key].append(sum_symbs/len(value))
    #         except:
    #             dict_for_print_w[key].append(None)
    #             dict_for_print_s[key].append(None)
    #     count+=1


def titles_statistics():
    
    # file1 = open('symbols_words_stats.txt', 'w')
    conn = sqlite3.connect('onepetro_metadata.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Metadata")
    data_aca=cursor.fetchall()
    fontsize_det = 13
    SEG_Conferences = {}
    SPE_Conference = {}
    SPE_Journals = {}
    All_Journals = {}
    All_Conferences = {}
    Total = {}
    
    for numbs in range(1980, 2021):
        SEG_Conferences[str(numbs)] = []
        SPE_Conference[str(numbs)] = []
        SPE_Journals[str(numbs)] = []
        All_Journals[str(numbs)] = []
        All_Conferences[str(numbs)] = []
        Total[str(numbs)] = []
    count = 0    
    for element in data_aca:
        if 'SEG Conf' in element[2]:
            SEG_Conferences[element[0]].append(element[3])
        if 'SPE Conf' in element[2]:
            SPE_Conference[element[0]].append(element[3])
        if 'SPE Jour' in element[2]:
            SPE_Journals[element[0]].append(element[3])
        if 'Jour' in element[2]:
            All_Journals[element[0]].append(element[3])
        if 'Conf' in element[2]:
            All_Conferences[element[0]].append(element[3])
        
        Total[element[0]].append(element[3])
    count=0
    slovary = [SPE_Conference, All_Conferences,  Total, SEG_Conferences, All_Journals, SPE_Journals]
    types = ['SPE Conferences', 'All Conferences', 'Total', 'SEG Conferences',  'All Journals',  'SPE Journals']
    dict_for_print_w = {}
    dict_for_print_s = {}
    for numbs in range(1980, 2021):
        dict_for_print_w[str(numbs)] = []
        dict_for_print_s[str(numbs)] = []
        
    for slovar in slovary:
        for key, value in slovar.items():
            sum_words = 0
            sum_symbs = 0
            if value == []:
                pass
            else:
                for titles in value:
                    sum_words = sum_words + titles.count(' ') + 1
                    sum_symbs = sum_symbs + len(titles)
            try:    
                dict_for_print_w[key].append(sum_words/len(value))
                dict_for_print_s[key].append(sum_symbs/len(value))
            except:
                dict_for_print_w[key].append(None)
                dict_for_print_s[key].append(None)
        count+=1
    
    # print('============Words============', file = file1)
    # print('Year', end = ' ',file = file1)
    # for names in types: print(names, end = ' ', file = file1)
    # print('', file = file1)

    # for key, value in dict_for_print_w.items():
    #     print(key, end = ' ', file = file1)
    #     for ii in value: print(ii, end = ' ', file = file1)
    #     print('', file = file1)
    
    # print('============Symbols============', file = file1)
    # print('Year', end = ' ',file = file1)
    # for names in types: print(names, end = ' ', file = file1)
    # print('', file = file1)

    # for key, value in dict_for_print_s.items():
    #     print(key, end = ' ', file = file1)
    #     for ii in value: print(ii, end = ' ', file = file1)
    #     print('', file = file1)
    
    # print(dict_for_print_w)
    
 
    

    # listin = [diction, types]
    # foo = Wrapper(listin)
    
    # print(foo)
    # quit()
    
    dict_for_graph_w = {}
    for element in types:
        dict_for_graph_w[element] = []
    
    for key, value in  dict_for_print_w.items():
        counter = 0
        for elementiy in types:
            dict_for_graph_w[elementiy].append(value[counter]) 
            counter+=1

    dict_for_graph_s = {}
    for element in types:
        dict_for_graph_s[element] = []
    
    for key, value in  dict_for_print_s.items():
        counter = 0
        for elementiy in types:
            dict_for_graph_s[elementiy].append(value[counter]) 
            counter+=1
    
      
  
# Here we are plotting the requestqed data on titles statistics
    colors = cm.rainbow(np.linspace(0.15, 1, len(dict_for_graph_w.keys())))
    s = list(range(1980, 2021, 1))
    fig = plt.subplots(figsize= (7.5, 5.0))
    # ax = plt.gca()
    counter_color = 0
    for k, v in dict_for_graph_w.items():
        
        plt.plot(s, v, linewidth=1.1, color=colors[counter_color], label = types[counter_color])
        counter_color +=1
    
    
    # ax.tick_params(axis = 'both', which = 'major', labelsize = fontsize_det)
    # ax.tick_params(axis = 'both', which = 'minor', labelsize = fontsize_det)
    # # Here we set the parameters of the figure
    plt.xlabel('Year', fontsize=fontsize_det)
    plt.ylabel('No. of words in title/No. of papers', fontsize=fontsize_det)
    plt.grid(True)
    plt.tight_layout()
    # The range of the axes
    plt.axis([1980, 2020, 7, 14], fontsize=fontsize_det)
    plt.legend(loc='upper left', fontsize=fontsize_det)
    # if len(lists[0]) > 3 and len(lists[1]) > 3:
    #     name = str(lists[0][:4] +'_' + lists[1][:4])
    # else:
    #     name = str(lists[0][:3] +'_' + lists[1][:3])
    # # print(name)
    plt.savefig('C:\\work\\Tex\\Presentation for weekly meeting\\images\\Title_stat.png', dpi=300)
    # plt.show()
    plt.close()
    
    fig = plt.subplots(figsize= (7.5, 5.0))
    # ax = plt.gca()
    counter_color = 0
    for k, v in dict_for_graph_s.items():
        
        plt.plot(s, v, linewidth=1.1, color=colors[counter_color], label = types[counter_color])
        counter_color +=1
    
    
    # ax.tick_params(axis = 'both', which = 'major', labelsize = fontsize_det)
    # ax.tick_params(axis = 'both', which = 'minor', labelsize = fontsize_det)
    # # Here we set the parameters of the figure
    plt.xlabel('Year', fontsize=fontsize_det)
    plt.ylabel('No. of symbols in title/No. of papers', fontsize=fontsize_det)
    plt.grid(True)
    plt.tight_layout()
    # The range of the axes
    plt.axis([1980, 2020, 60, 105], fontsize=fontsize_det)
    plt.legend(loc='upper left', fontsize=fontsize_det)
    # if len(lists[0]) > 3 and len(lists[1]) > 3:
    #     name = str(lists[0][:4] +'_' + lists[1][:4])
    # else:
    #     name = str(lists[0][:3] +'_' + lists[1][:3])
    # # print(name)
    plt.savefig('C:\\work\\Tex\\Presentation for weekly meeting\\images\\Title_stat_sym.png', dpi=300)
    # plt.show()
    plt.close()

def grams_creation():
    
    # file1 = open('symbols_words_stats.txt', 'w')
    conn = sqlite3.connect('onepetro_metadata.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Metadata")
    data_aca=cursor.fetchall()
    fontsize_det = 13
    SEG_Conferences = {}
    SPE_Conference = {}
    SPE_Journals = {}
    All_Journals = {}
    All_Conferences = {}
    Total = {}
    
    for numbs in range(1980, 2021):
        SEG_Conferences[str(numbs)] = []
        SPE_Conference[str(numbs)] = []
        SPE_Journals[str(numbs)] = []
        All_Journals[str(numbs)] = []
        All_Conferences[str(numbs)] = []
        Total[str(numbs)] = []
    count = 0    
    for element in data_aca:
        if 'SEG Conf' in element[2]:
            SEG_Conferences[element[0]].append(element[3])
        if 'SPE Conf' in element[2]:
            SPE_Conference[element[0]].append(element[3])
        if 'SPE Jour' in element[2]:
            SPE_Journals[element[0]].append(element[3])
        if 'Jour' in element[2]:
            All_Journals[element[0]].append(element[3])
        if 'Conf' in element[2]:
            All_Conferences[element[0]].append(element[3])
        
        Total[element[0]].append(element[3])
    count=0
    slovary = [SPE_Conference, All_Conferences,  Total, SEG_Conferences, All_Journals, SPE_Journals]
    types = ['SPE Conferences', 'All Conferences', 'Total', 'SEG Conferences',  'All Journals',  'SPE Journals']
    
    for key, value in Total.items():
        print(len(value), end = ', ')
    # for files in range(1980, 2021):
    #     file001 = open('C:\\work\\SQL\\gramms_onepetro\\'+str(files)+'.txt', 'w')
                       
    #     full_string = ''
    #     for titel in Total[str(files)]:
    #         full_string = full_string + titel + '\n'
        
    #     print(full_string, file = file001)

    quit()        
    
    
def authors_statistics():
    file2 = open('authors_stats.txt', 'w')
    
    conn = sqlite3.connect('onepetro_metadata.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Metadata")
    data_aca=cursor.fetchall()
    Authors_all = {}
    Authors_Conferences = {}
    Authors_Jounals = {}
    Authors_list = []
    
    for numbs in range(1980, 2021):
        Authors_all[str(numbs)] = []
        Authors_Conferences[str(numbs)] = []
        Authors_Jounals[str(numbs)] = []
    count =0
    for element in data_aca:
        if 'Conf' in element[2]:
            Authors_Conferences[element[0]].append(eval(element[5]))
        if 'Jour' in element[2]:
            Authors_Jounals[element[0]].append(eval(element[5]))
        
        for author in eval(element[5]):
            Authors_all[element[0]].append(author)
            Authors_list.append(str(author))
    
    # for key, value in Authors_all.items():
    #     print(key, len(value))
    Authors_list = sorted(Authors_list)

    all_dicty = dict(Counter(Authors_list))
    print(type(all_dicty))
    # for key, value in all_dicty.items():
    #     print(value, key, file = file2)
    
    print(len(all_dicty))
    
    
    # output table: year, number of papers, average length in words, average length in symbols
      
    #     for titles in value:
    #     words_count = titles.count(' ') + 1
    #     titles.count(' ') + 1
    #     # text = text + ' ' + str(titles) 
    #     summs = summs + len(titles)
    # # print(keym, summs/len(value))    
    # summs = 0
    # print(text)
    # # print(keym, value)    
    # quit()

societies()
quit()
# onepetro_title_length_symbols = [68.03480475382004, 70.51317829457365, 70.61430967020682, 69.09188660801564, 69.22069377990431, 69.94703511801957, 71.5746835443038, 70.22718214428059, 71.48124191461837, 71.7446724546172, 71.0291149068323, 71.18088357877188, 73.17242582897033, 73.82437826220448, 74.27141645462257, 75.33218092768655, 77.17460695569319, 76.39401553220648, 75.97220354180676, 75.81510081510082, 76.0386615811373, 77.46501885211562, 78.62071697365815, 79.0485012489592, 79.8725172274017, 81.0240067624683, 81.7263177294508, 81.6072343149808, 82.76188264437219, 84.66856439452224, 86.00889437924644, 85.94849393662798, 86.41653722069542, 88.86747931111609, 89.53688888888888, 91.19462770970782, 92.63178182519033, 93.44645491198742, 94.24398291925466, 96.02434312210201, 95.45503791982665]
# onepetro_aver_coauth_numb =  [2.094227504, 2.117829457, 2.117384013, 2.107038123, 2.133373206, 2.127806563, 2.144303797, 2.146671981, 2.21992238, 2.241515391, 2.345496894, 2.327035288, 2.460732984, 2.487258213, 2.476957874, 2.647363872, 2.7060505, 2.676107812, 2.733243667, 2.749034749, 2.762482663, 2.814201927, 2.912854031, 2.989383847, 3.052290231, 3.038546069, 3.112790269, 3.141645327, 3.197398978, 3.233728266, 3.386411365, 3.361585604, 3.45047198, 3.527063297, 3.615209877, 3.743638077, 3.809867977, 3.921231193, 4.026688665, 4.210490726, 4.13163597]
fontsize_det = 13
start_year = 1980
end_year = 2020
# Academy dictionaty
start_time = time.time()

conn = sqlite3.connect('onepetro_metadata.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Metadata")
data_aca=cursor.fetchall()

onepetro_metadata = {}

onepetro_dict_affs = {}
onepetro_dict_auths = {}
onepetro_dict_titles = {}
coauth_ave = {}
for numbs in range(1980, 2021):
    onepetro_dict_affs[str(numbs)] = []
    onepetro_dict_auths[str(numbs)] = []
    onepetro_dict_titles[str(numbs)] = []
    onepetro_metadata[str(numbs)] = []
    coauth_ave[str(numbs)]  = []
    onepetro_metadata 

count = 0

for element in data_aca:
    onepetro_dict_titles[element[0]].append(element[3])

for element in data_aca:
    for comp in eval(element[4]):
        onepetro_dict_affs[element[0]].append(comp)
    
    for name in eval(element[5]):
        onepetro_dict_auths[element[0]].append(name)
    count +=1

total_auths_list=[]
total_comp_list = []
for key, value in onepetro_dict_auths.items():
    coauth_ave[key].append(len(value))
    for lists in value:

        total_auths_list.append(str(lists))

for key, value in onepetro_dict_affs.items():
    for lists in value:
        total_comp_list.append(str(lists))
    

# for keym, value in onepetro_dict_titles.items():
#     for els in coauth_ave[keym]:
#         print(els/len(value))
summs = 0  
text = ''
words_count = 0
for keym, value in onepetro_dict_titles.items():
    for titles in value:
        words_count = titles.count(' ') + 1
        titles.count(' ') + 1
        # text = text + ' ' + str(titles) 
        summs = summs + len(titles)
    # print(keym, summs/len(value))    
    # summs = 0
    # print(text)
    # # print(keym, value)    
    # quit()
counter = 0
# for items in total_auths_list:
    
#     if 'Eltsov' in items:
#         print(items, total_comp_list[counter])
#     counter+=1
        # print(key, len(value))
    # for lists in value:
# most_common = [item for item in Counter(total_auths_list).most_common(50000)]
# for elemelo in most_common:
#     if 'Patzek' in str(elemelo):
#         print(elemelo)

print("--- %s seconds ---" % (time.time() - start_time))


# most_common = [item for item in Counter(total_comp_list).most_common(100)]
# for eleme in most_common:
#     print(eleme)

# print("--- %s seconds ---" % (time.time() - start_time))


