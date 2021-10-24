import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.A69aGMvxxpYesQN5ORGR63jShl09XefhRsRmwrHTmNUp3ZUvXW3RgQSvwXxKjXUm-n313Vy_4gDuDrLF2Hq6pI-RvUMLe2AHRkV6epemcchlXB1SpNr_Tm14eeYa3V7dAUxFIPM'
    transferData=TransferData(access_token)

    file_from=input("enter the file to tansfer: ")
    file_to=input("enter the path to upload: ")

    transferData.upload_file(file_from,file_to)
    print("the file has been moved")

main()