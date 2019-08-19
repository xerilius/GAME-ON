##################################################################
# and print it(replace with insert statement) with sql alchemy
# offset to get the next set

# Filters: 
    # "f name, genres; where id = 12343;
    #/games/
    # search "zelda"; where rating >=80 & release_dates.date > ;
# sort : "fields *; sort popularity asc/desc"
# sort: "f * ; s popularity asc/desc"
# sort release_dates.date desc; where rating >=90;

# fields: "f name, release_dates, genres.name,rating;"

# where: fields *; where genres = 4; 
# where : "f *; w genres = 4;"
# do fields name, genres.name; where id = 1942;
# f name, release_dates, genres.name,rating; w id = (435,23,143)

# for games :
# search : search "Halo"; fields name; or f name;
# same as:




# if __name == '__main__':

#     # To activate debugger toolbar
#     app.debug = True

#     connect_to_db(app)

#     # Use the DebugToolbar
#     DebugToolbar(app)

#     app.run(host='0.0.0.0')



    # step1 : create  flask requests to API
    # step2 : install all modules required (ex)pip3 install requests) 
    #           via GitBash
    # step3 : pip3 freeze > requirements.txt
    # step4 : make model tables
    # step5 : parse data and insert with sql alchemy

        # create new data_file.json file with write mode 
        # with open('game_data.txt', 'w') as text_file:
        #     # write json data into file
        #     json.dump(game_data, text_file)