import json

class Log_analyzer:

    def __init__(self,filename,outputfile):
        self.filename=filename
        self.outputfile=outputfile

    def read_logs(self):
        try:
            with open(self.filename,"r") as file:
                lines=file.readlines()

                if not lines:
                    print(f"{self.filename} is empty")
                    return []
                
                return lines
        except FileNotFoundError:
            print(f"{self.filename} file not found")
            return []
        
    def analyze(self):
        log_count={
            "INFO" : 0,
            "WARNING" : 0,
            "ERROR" : 0
        }

        lines=self.read_logs()

        if not lines:
            return
        
        for line in lines:
            if "INFO" in line:
                log_count["INFO"] +=1
            elif "WARNING" in line:
                log_count["WARNING"] += 1
            elif "ERROR" in line:
                log_count["ERROR"] += 1

        print(f"\nSummary for {self.filename}: ")
        print(log_count)

        self.write_json(log_count)

    def write_json(self,json_object):
        try:
            with open(self.outputfile,"w+") as json_file:
                json.dump(json_object,json_file,indent=4)
        except Exception as e:
            print("Error writing JSON: ",e)

if __name__ == "__main__":
    log1=Log_analyzer("app.log","out.json")
    log1.analyze()