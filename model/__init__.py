
def sqlQueries(query):
    if query is not None:
        if type(query) == list:
            list_dic = []
            for index in range(len(query)):
                dic = removeInstanceState(query[index].__dict__)
                list_dic.append(dic)
            return list_dic
        else:
            obj = query.__dict__
            return removeInstanceState(obj)
    else:
        return None


def removeInstanceState(obj):
    if type(obj) == dict:
        del obj['_sa_instance_state']
        return obj
    else:
        return obj
