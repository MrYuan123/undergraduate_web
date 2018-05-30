#!/usr/bin/python3
# -*-coding:utf-8 -*-
import math,csv,traceback,pymysql


def get_list(ID):
    print('get_list')
    try:
        db = pymysql.connect("localhost","root","Yyk19951006+","undergraduate" )
        db.set_charset('utf8')
        cursor = db.cursor()
    except Exception:
        traceback.print_exc()
        print("connection fail!")
        return None

    sql_command = 'select * from userCF where ID =' + ID  + ";"
    print(sql_command)

    try:
        cursor.execute(sql_command)
        results = cursor.fetchall()
        # results = results[:MAXmovies]
        # for item in results:
        #     return_list.append(item[1])
        #     print(item)
        item = results[0][1]
        items = item.split(',')
        return_list = list()
        for item in items:
            detail =  item.replace('[','').replace(']','').replace(' ','').replace('\'','')
            return_list.append(detail)

        return return_list
    except:
        print("sort fail!")
        return_list = None
        return return_list

def get_movies(movielist):
    if movielist == None:
        print('No movie!')
        return None
    print('get_movies')
    return_movies = list()
    try:
        db = pymysql.connect("localhost","root","Yyk19951006+","undergraduate" )
        db.set_charset('utf8')
        cursor = db.cursor()
    except Exception:
        traceback.print_exc()
        print("connection fail!")
        return None

    for movieId in movielist:
        sql_command = 'select * from movies where movieId=' + movieId + ';'
        try:
            cursor.execute(sql_command)
            results = cursor.fetchall()
            detail = results[0]
            return_movies.append(detail)
        except:
            print("sort fail!")
            return_movies = None
            return return_movies

    return return_movies

def get_history(ID):
    history_list = list()
    try:
        db = pymysql.connect("localhost","root","Yyk19951006+","undergraduate" )
        db.set_charset('utf8')
        cursor = db.cursor()
    except Exception:
        traceback.print_exc()
        print("connection fail!")
        return None

    sql_command = 'select * from ratingsA where userId = ' + ID + ';'
    try:
        cursor.execute(sql_command)
        results = cursor.fetchall()
        history_list = results
    except:
        print("sort fail!")
        history_list = None
        return history_list

    return history_list

def get_final_list(ID):
    history_list = get_history(ID)
    temp = list()
    for item in history_list:
        temp.append(item[1])

    movielists = get_movies(temp)
    final_list = list()
    for item in movielists:
        for n in history_list:
            if item[0] == n[1]:
                temp = list()
                temp.append(item[0])
                temp.append(item[1])
                temp.append(item[2])
                temp.append(str(n[2]))
                final_list.append(temp)
                break

    return final_list

def most_popular():
    details = ['356', '296', '318', '593', '260', '480', '2571', '1', '527', '589', '1196', '110', '1270', '608', '2858', '1198', '780', '1210', '588','457', '2959', '590', '4993', '858', '50', '47', '150', '364', '380', '32']
    # with open('most_popular.csv','r') as f:
    #     csv_file = csv.reader(f)
    #     for item in csv_file:
    #         details.append(item[0])
    return details

# if __name__ == '__main__':
#     print(most_popular())
