"""
reading logs, analyzing it and write the the results in a proper json output file
"""

# import json

# def read_logs():
#     with open("app.log","r") as file:
#         return file.readlines()

# def analyze(lines):
#     log_count={
#         "INFO":0,
#         "WARNING":0,
#         "ERROR":0
#     }

#     for line in lines:
#         if "INFO" in line:
#             log_count["INFO"]+=1
#         elif "WARNING" in line:
#             log_count["WARNING"]+=1
#         elif "ERROR" in line:
#             log_count["ERROR"]+=1
#         else:
#             pass

#     return log_count

# def write_json(counts):
#     with open("output.json","w+") as json_file:
#         json.dump(counts,json_file)

# lines=read_logs()
# counts=analyze(lines)
# write_json(counts)


"""
doing the same thing but with class and objects
"""

import json

class Log_analyzer:
    
    def __init__(self,file_name,output_file):
        self.file_name=file_name
        self.output_file=output_file

    def read_logs(self):
        with open(self.file_name,"r") as file:
            return file.readlines()

    def analyze(self):
        log_count={
            "INFO":0,
            "WARNING":0,
            "ERROR":0
        }

        lines = self.read_logs()

        for line in lines:
            if "INFO" in line:
                log_count["INFO"]+=1
            elif "WARNING" in line:
                log_count["WARNING"]+=1
            elif "ERROR" in line:
                log_count["ERROR"]+=1
            else:
                pass

        self.write_json(log_count)

    def write_json(self,json_object):
        with open(self.output_file,"w+") as json_file:
            json.dump(json_object,json_file)

log1= Log_analyzer("app.log","output.json")
log1.analyze()

log2= Log_analyzer("app2.log","output2.json")
log2.analyze()