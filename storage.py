import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BEJmXQHOKg_HfayydnUnSxd3_O4ff8svoaR3WTlMaR0xPOosjX-rV75PlfUW9EJeZwU6pIbu1L-b_wqQaOAIQIivrAn3eNmo8OQFLNMG3b-61IzMvkADuSg3gn-jJqYDolRvaLFF'
    transferData = TransferData(access_token)

    file_from = input('Enter the path of file to be uploaded')
    file_to = input('ENter the path where the file has to be uploaded')  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

main()