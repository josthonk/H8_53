def make_students(names):
    students = {}
    for i in range (1,len(names)+1):
        students[i] = names [i-1]
    return students

bootcamp_name="hactiv8"
id_to_students = {
    1: "Yusuf",
    2: "Satya",
    3: "Richard",
    4: "Steffany",
    5: "Timothius",
    6: "Yosua MGS",
}

list_names = ["john","star","lucifer","morning"]

print("Nama BootCamp: ", bootcamp_name)
print("List Nama: ", list_names)
print("Student's Name with ID: ", id_to_students)