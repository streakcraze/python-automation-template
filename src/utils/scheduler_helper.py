import schedule  # Import the schedule library for task scheduling
import time  # Import the time library for sleep functionality

def schedule_job_every_five_minutes(job):
    # Schedule the given job every five minutes
    schedule.every(5).minutes.do(job)  # Schedule the job function to run every five minutes

    while True:
        schedule.run_pending()  # Run all scheduled tasks that are due
        time.sleep(1)  # Sleep for 1 second before checking again

def schedule_job_every_minute(job):
    # Schedule the given job every minute
    schedule.every(1).minute.do(job)  # Schedule the job function to run every minute

    while True:
        schedule.run_pending()  # Run all scheduled tasks that are due
        time.sleep(1)  # Sleep for 1 second before checking again
