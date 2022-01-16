import gistyc

class Gist():
    def __init__(self):
        self.AUTH_TOKEN = "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" 
        self.gist_api = gistyc.GISTyc(auth_token=self.AUTH_TOKEN)
        self.file_names = []
        self.filepath_list = []
        self.response_datas = []
    def Create(self):
        for FILEPATH in self.filepath_list:
            print(FILEPATH)
            response_data = self.gist_api.create_gist(file_name=FILEPATH)
            self.response_datas.append(response_data)
        #print(self.response_datas)
    def get_All_Gist(self):
        return self.gist_api.get_gists()
    def make_Scripts_Str(self):
        self.Gist_scripts = {}
        Gist_list = self.get_All_Gist()
        for i in Gist_list:
            for j in self.file_names:
                if j in i['files']: # 올린 파일을 찾으면 
                    print(i['html_url'])
                    self.Gist_scripts[j] = "<script src={0}></script>".format(i['html_url'] + ".js")