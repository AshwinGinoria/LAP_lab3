class check_keys:
    def check_keywords(path_file, path_keywords, ext):
        list_path_keywords = []

        output_dictionary = {}

        temp_keywords = open(path_keywords + ext, "r")
        for line in temp_keywords:
            word_list = line
            word_list = word_list.split()
            for entry in word_list:
                list_path_keywords.append(entry)
        temp_keywords.close()
        temp_output = open(path_file + "output" + ext, "w")
        temp_file = open(path_file + ext, "r")
        for line in temp_file:
            temp_str = ""
            for word in list_path_keywords:
                if word in line.split():
                    temp_str += "," + word
            if temp_str != "":
                if line[-1:] == "\n":
                    output_dictionary[temp_str[1:]] = (line)[:-1]
                else:
                    output_dictionary[temp_str[1:]] = line
                temp_output.write(temp_str[1:] + " : " + line)

        return output_dictionary
