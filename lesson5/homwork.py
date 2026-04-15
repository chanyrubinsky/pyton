#import os


# os.mkdir('mewFolder')
def deleteFolder():
    try:
        os.rmdir('mew folder')
        print(f"התיקיה {'mew folder'} נמחקה בהצלחה.")
    except OSError as e:
        print(f"שגיאה במחיקת התיקיה {'mew folder'}: {e}")


# deleteFolder()


def create_file(link, f):
    file = os.path.join(link, f)
    os.makedirs(link, exist_ok=True)
    with open(file, 'w') as f:
        f.write("")

def write_in_file():
    file = open("file.txt", "w")

    # כתוב טקסט לקובץ
    file.write("שלום, זה הטקסט שייכתב לקובץ.\n")
    file.write("זה שורה חדשה.\n")

    # סגור את הקובץ
    file.close()


write_in_file()
#create_file('Z:\יד תשפו\רובינסקי חנה\piton\pyton\lesson5', 'file.txt')
