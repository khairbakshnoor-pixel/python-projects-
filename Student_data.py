student_name=input("enter the student name     :")
class_conducted=int(input("how many classes are conducted   :"))
class_attended=int(input("how many classes are attended     :"))
marks=int(input("enter marks out of 100                     :"))
data={
"student":student_name,
"total classes conducted":class_conducted,
"total classes atended":class_attended,
"marks":marks
}

attendance_percent=(class_attended/class_conducted)*100
print("attendance percentage",attendance_percent)
print(data.get("student"))
percent=(marks/100)*100
if class_attended<75:
    print("student is  eligible ")

    if percent>85:
        print("A grade")
    elif percent>70 and percent<84:
        print("B grade")
    elif percent>50 and percent< 69:
        print("c grade")
    elif percent<50:
        print("failed")
else:
    print("not eligible")

print(data)