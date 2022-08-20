import json
import os.path


def main():
    fileList = []
    path = 'sample_movie'
    for filenames in os.walk(path):
        fileList.append(filenames)

    data_list = []

    for i in range(len(filenames[2])):
        try:
            data = json.load(open('sample_movie/' + filenames[2][i], encoding='utf-8'))
            data_final = dict((k, data[k]) for k in ('original_title', 'budget', 'genres', 'popularity', "release_date",
                                                     "revenue", "runtime", "vote_average", "vote_count", "spoken_languages"))
            genres = []
            for i in range(len(data_final["genres"])):
                genres.append(data_final["genres"][i]['name'])
            data_final["genres"] = ", ".join(genres)

            spoken_languages = []
            for i in range(len(data_final["spoken_languages"])):
                genres.append(data_final["spoken_languages"][i]['name'])
            data_final["spoken_languages"] = ", ".join(spoken_languages)

            data_list.append(data_final)
        except Exception:
            pass

    out_file = open("movies.json", "w")
    json.dump(data_list, out_file, indent=2)
    out_file.close()


if __name__ == '__main__':
    main()

