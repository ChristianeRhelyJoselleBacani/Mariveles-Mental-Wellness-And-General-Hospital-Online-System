# Mariveles Mental Wellness and General Hospital Online System
# Created by : Christiane Rhely Joselle A. Bacani
print("Welcome to Mariveles Mental Wellness and General Hospital Online System!")
pressEnter = input("Press enter to start : ")

print("\n1.) Psychiatric Admission\n2.) Psychiatric Consultation\n3.) Medical Consultation\n4.) Laboratory\n5.) About\n6.) Exit")
userChoose = int(input("Enter your choice : "))

if userChoose == 1:
    print("PSYCHIATRIC ADMISSION!")
    patientName = input("Enter Patient`s Name : ")
    patientMiddleName = input("Enter Patient`s Middle Name : ")
    patientSurname = input("Enter Patient`s Surname : ")

    reason = input("Enter reason the reason why patient/s need to admit : ")

    doctorName = input("Enter the full name of doctor on duty on the day the patient admitted : ")
    nurseName = input("Enter the full name of nurse on duty on the day the patient admitted : ")
    date = input("Enter today`s date : ")

    System.out.print("Patient Successfully Admitted!")

elif userChoose == 2:
    print("PSYCHIATRIC CONSULTATION!")
    patientName = input("Enter Patient`s Name : ")
    patientMiddleName = input("Enter Patient`s Middle Name : ")
    patientSurname = input("Enter Patient`s Surname : ")

    print("Please wait for the doctor for your online consultation, thank you!")

elif userChoose == 3:
    print("MEDICAL CONSULTATION!")
    patientName = input("Enter Patient`s Name : ")
    patientMiddleName = input("Enter Patient`s Middle Name : ")
    patientSurname = input("Enter Patient`s Surname : ")

    print("Please wait for the doctor for your online consultation, thank you!")

elif userChoose == 4:
    print("LABORATORY!")
    laboratoryTest = input("Enter what laboratory test you need : ")

    print("Go to the cashier to pay your bills, thank you!")

elif userChoose == 5:
    print("Welcome to Mariveles Mental Wellness and General Hospital Online System!\n\nAt Mariveles Mental Wellness and General Hospital, we are committed to providing\ncomprehensive healthcare services with a special focus on mental well-being. Our\nonline system is designed to enhance your healthcare experience by offering\nconvenient and accessible services from the comfort of your home.\n")

elif userChoose == 6:
    print("Sucessfully Exited!")

else:
    print("Invalid Choice!")

















































