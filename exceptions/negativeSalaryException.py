class NegativeSalaryException(Exception):
    pass
def calculate_average_salary(JobListing):
    try:
        total_salary=0
        valid_job_listing=0
        for job in jobListing:
            if job['salary']<0:
                raise NegativeSalaryException(job['job_title'])
                total_salary += job['salary']
                valid_job_listing += 1
            
            if valid_job_listing == 0:
                raise ZeroDivisionError("no valid job listing found with non- negavtive salary")

            average_salary= total_salary/valid_job_listing
            print(f"Average salary: {average_salary}")

    except NegativeSalaryException as  e:
        print(f"Error occured salary can not br negative: {e}")

    except ZeroDivisionError as e:
        print(f"Error: {e}")