from dao.createTables import createTable
from dao.insertCompany import InsertCompany
from dao.insertJobListing import InsertJobListing
from dao.insertApplicant import InsertApplicant
from dao.insertJobApplicant import InsertJobApplication
from dao.getJobListings import GetJobListings
from dao.getCompanies import GetCompanies
from dao.getApplicants import GetApplicants
from dao.getJobApplications import GetApplicationsForJob
from dao.salaryRange import search_by_salary_range
if __name__=="__main__":
    try:
        createTable()
        while True:
            print("Enter 1 to insert new company")
            print("Enter 2 to insert new job listing")
            print("Enter 3 to insert new applicant")
            print("Enter 4 to insert new job applications")
            print("Enter 5 to get job listings")
            print("Enter 6 to get Companies")
            print("Enter 7 to get Applicants")
            print("Enter 8 to get job applications")
            print("Enter 9 to get salary in range")
            print("Enter 10 to exit")
            c=input("Enter choice: ")
            if c=="1":
                InsertCompany()
            elif c=="2":
                InsertJobListing()
            elif c=="3":
                InsertApplicant()
            elif c=="4":
                InsertJobApplication()
            elif c=="5":
                GetJobListings()
            elif c=="6":
                GetCompanies()
            elif c=="7":
                GetApplicants()
            elif c=="8":
                GetApplicationsForJob()
            elif c=="9":
                search_by_salary_range()    
            elif c=="10":
                break
            else:
                print("Invalid Choice")
    except Exception as e:
        print(f"An error has occured: {e}")