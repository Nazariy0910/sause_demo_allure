from datetime import datetime
def log(action, status):
    date_time = datetime.now().strftime("%H:%M:%S")

    clean_status= status.lower()

    if clean_status == 'passed':
        print(f'{date_time}💫 Passed {action}')
    elif clean_status == 'failed':
        print(f'{date_time}❌ Failed {action}' )
    else:
        print(f'{date_time}⚠️ Unknown status')

log("Open main page", "passed")
log("Click Login button", "PASSED" )
log("Find Buy button", "failed")
log("Check header", "PASSED")
