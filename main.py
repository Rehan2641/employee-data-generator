import pandas as pd
import faker
import random
import datetime

fake = faker.Faker('en_in')
dep = ['IT','HR','Sales','Finance','Markeing','Management','Supervisor','Operations','Customer Service','Administration']
ran = ["South","West","East","North"]
Type = ["Full-Time","Part-Time"]

employee_data = {
    'Employee Name':[fake.name() for a in range(1000)],
    "Employee ID":[random.randint(1000,9999) for z in range(1000)],
    "Email":[fake.email() for x in range(1000)],
    "Phone NO.":["+91" + str(random.randint(6000000000, 9999999999)) for x in range(1000)],
    "City":[fake.city() for f in range(1000)],
    "Salary":[random.randint(20000,40000) for s in range(1000)],
    "Date of joinig":[fake.date_between(start_date=datetime.date(2016, 1, 1), end_date=datetime.date(2025, 12, 31)) for z in range(1000)],
    "Region":[random.choice(ran) for z in range(1000)],
    "Department":[random.choice(dep) for z in range(1000)],
    "Account Number":["Ac." + str(random.randint(100000000000,999999999999)) for t in range(1000)],
    "Employment Type":[random.choice(Type) for z in range(1000)],
    "Age":[random.randint(25,45) for z in range(1000)],
    "IFSC Code": [f"IDFB00{fake.numerify(text='######')}" for z in range(1000)]
}
frame_work = pd.DataFrame(employee_data)
print(frame_work)
frame_work.to_excel("Employee Sheet_Data.xlsx",index=False)

