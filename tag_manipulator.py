class TagManipulator():
    def parse_string(self, tags):
        result = []

        if len(tags) < 1 :
            return result

        result = tags.split(",")
        #result.append(tags)
        for index in range(0,len(result)):
            new_entry = result[index].strip()
            result[index] = new_entry


        return result