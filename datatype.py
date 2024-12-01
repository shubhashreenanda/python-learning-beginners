from driverslicenseapplication import firstName, lastName

id=1
firstName="john"
lastName="behera"
ssn="123-456-7890"
hasInsurance=True
billingAmount="10000"
print(type(billingAmount))
billingAmount=float(billingAmount)
print(type(billingAmount))

print(id,firstName,lastName,ssn[8:len(ssn)],billingAmount)