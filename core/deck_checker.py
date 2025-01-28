print("\033[94mStarting app...\033[0m")
from datetime import datetime
import random
import time
from utils.browser import get_browser
from selenium.webdriver.common.by import By
from utils.twilio_client import send_message
from enums.steam_deck_model import SteamDeckModel
from config.settings import DEBUG_MODE_ON, SEND_FAILURE_NOTIFICATION_BY_SMS, CHECK_INTERVAL, STORE_URL, TWILIO_TO_NUMBER, TWILIO_FROM_NUMBER, REQUIRED_MODEL #Do not remove these, even if claimed to be unused.
from selenium.webdriver.support import expected_conditions as EC

#Log configuration
start_time = datetime.now() # for community info, people might want to know how long it took you :)

#Debug specific stuff
max_debug_attempts = 20
fake_in_stock_chance = 0.10 #10% chance of simulating stock in DEBUG mode.
fake_error_chance = 0.03 #3% chance of simulating an error in DEBUG mode.

#Confirm running and configuration
print(f"\033[94mI am now looking for Steam Deck stock. \n- I will check {STORE_URL} every {CHECK_INTERVAL} seconds. \n- I started at: {start_time}. \n- Any logging information in \033[97mwhite\033[94m can be safely ignored, please only refer to the coloured messages.\033[0m")
if DEBUG_MODE_ON:
    print(f"\033\n[93m!!! WARNING - YOU ARE IN DEBUG MODE: !!! \nI am running in debug mode, so the following apply: \n- The max number of stock checks before I stop is {max_debug_attempts}. \n- I will check every 5 seconds and ignore your setting. \n- I will show you the browser and scroll to the stock area. \n- I will also simulate 'in stock' alerts and 'errors' based on a low random chance, to prove I'd work. \n- I will not send SMS messages to you in this mode, you will NOT spend Twilio credits. \n- The app will display additional details in the output area (console).\nNOTE: If you are wanting to use the app properly, you should disable DEBUG mode by setting it to False in the .env file.\033[0m" )
    CHECK_INTERVAL = 5 #For convenience we'll override CHECK_INTERVAL to be much faster, when debugging, so you don't have to wait ages.

#Launches the looping stock check process
def check_deck():
    stock_check_attempt = 0    
    driver = get_browser()
    driver.get(STORE_URL)
    required_model_parsed = None

    #Which model is the user looking for?
    if REQUIRED_MODEL.lower()  == "any":
        required_model_parsed = "any"
        print(f"\033[94mYou have chosen to find ANY Steam Deck stock, not a specific model.\033[0m")
    else:
        required_model_parsed = SteamDeckModel[REQUIRED_MODEL].value
        print(f"\033[94mYou have chosen to find one specific model, the {REQUIRED_MODEL}.\033[0m")

    #Setup loop to check for stock until found or crashed.
    stock_not_found = True
    while stock_not_found:
        try:
            stock_check_attempt += 1

            if DEBUG_MODE_ON and stock_check_attempt == max_debug_attempts: 
                #Stops people running app in debug mode infinitely, by breaking after max_debug_attempts.
                print(f"\033[91mDEBUG INFO: Attempt {stock_check_attempt}: I have reached the maximum number of attempts in debug mode, so I am stopping now. You can change this in the .env file.\033[0m")
                break 

            print(f"\033[94mAttempt {stock_check_attempt}: Checking for Steam Deck model availability...\033[0m")
            result = runner(stock_check_attempt, driver, required_model_parsed)
            if result["status"]:
                # Notify user that stock is found, end process, log.
                message = (
                    f"Your chosen Steam Deck model '{REQUIRED_MODEL}' is now in stock!!!\n"
                    f"Link to Steam Store: {STORE_URL}.\n"
                    f"Time taken to find stock: {result['time_to_find']}.\n"
                    f"Attempt(s) before stock found: {stock_check_attempt}.\n"
                    f"The app is now stopping and would need to be manually restarted if you still need it."
                )
                print(f"\033[94mAttempt {stock_check_attempt}: Steam Deck model '{REQUIRED_MODEL}' found in stock after {result['time_to_find']}. Sending you an SMS...\033[0m")
                if DEBUG_MODE_ON:
                    print(f"\033[93mDEBUG INFO: Attempt {stock_check_attempt}: Stock was found, but I am not sending you an SMS, to save money. I would have notified you if DEBUG were False. Here is what I would have sent to '{TWILIO_TO_NUMBER}' from '{TWILIO_FROM_NUMBER}' saying: '{message}'\033[0m")
                else:
                    send_message(
                        TWILIO_TO_NUMBER,
                        TWILIO_FROM_NUMBER,
                        message
                    )
                with open("stock_check_log.txt", "a") as log_file:
                    log_file.write(f"Stock found at {datetime.now()} while looking for model: '{REQUIRED_MODEL}' after {stock_check_attempt} attempt(s). Would have sent this message: \nTo: {TWILIO_TO_NUMBER} \nFrom: {TWILIO_FROM_NUMBER} \nMessage: {message}\n")
                stock_not_found = False
                break

        except Exception as e:
                #Print out error, make error log file and potentially send SMS if we're not debugging and user enabled that option.
                print(f"\033[91mError during attempt {stock_check_attempt}: {e}\033[0m")
                if not DEBUG_MODE_ON and SEND_FAILURE_NOTIFICATION_BY_SMS:
                    error_message = str(e)[:100] + '...' if len(str(e)) > 100 else str(e) #Just the first 100 chars to prevent spam.
                    send_message(
                        TWILIO_TO_NUMBER,
                        TWILIO_FROM_NUMBER,
                        (
                            "Your app checking for Steam Deck models crashed. \n"
                            f"Attempt(s) before crash: {stock_check_attempt}. \n"
                            f"Duration before crash: {datetime.now() - start_time}. \n"
                            f"The app is now stopping and would need to be manually restarted if you still need it. \n"
                            "Please investigate. The start of the error was: \n"
                            f"{error_message}..."
                        )
                    )
                with open("error_log.txt", "a") as error_log_file:
                    error_log_file.write(f"Error at {datetime.now()} during attempt {stock_check_attempt} while looking for model: '{REQUIRED_MODEL}': {e}\n")
                raise Exception
        
        #Wait for the next check interval before looping.
        time.sleep(CHECK_INTERVAL) 

#Interacts with the webpage and gets data regarding stock levels
def runner(attempts, driver, required_model_parsed):
    #Const to find the sale section on the page. This is the XPATH of the sale section, e.g. we're looking for on the page. If Valve ever change this, app breaks. This is where the models are listed.
    SALE_SECTION_XPATH = "//*[@id='SaleSection_33131']"

    if attempts > 0:
        #refresh the page each run, but only after the first.
        driver.refresh()

    # Let page load until the products are visible.     
    random_sleep_time = random.randint(3, 7)
    time.sleep(random_sleep_time)

    #Target models
    all_models_on_page = driver.find_elements(By.XPATH, SALE_SECTION_XPATH)[0].text 

    if DEBUG_MODE_ON:
        print(f"\033[93mDEBUG INFO: Attempt {attempts}: Browser is open, scrolling down to the stock section...\033[0m")
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, SALE_SECTION_XPATH)) #scroll to the listings if we're debugging
        if random.random() < fake_error_chance:
            print(f"\033[93mDEBUG INFO: Attempt {attempts}: For this run, we are randomly generating exception to simulate failure, based on a very low random chance. This is so you can see what it 'would' do when an error happens...\033[0m")
            raise Exception("Randomly generated exception for testing purposes. I'm not a real error!") #Low chance during DEBUG mode, to raise a generic exception and test failure logic.

    #TRUE: We're looking for any stock at all, we don't care about the model.
    we_want_any_stock = REQUIRED_MODEL.lower() == "any"
    if we_want_any_stock:
        # Simulate stock availability with a low chance during debug mode for testing purposes.
        if DEBUG_MODE_ON and random.random() < fake_in_stock_chance:
            print(f"\033[93mDEBUG INFO: Attempt {attempts}: For this run, we are simulating a real 'in stock' message on the webpage, for any model, based on a low random chance. This is so you can see what it 'would' do when there is ANY new stock...\033[0m")
            all_models_on_page = all_models_on_page.replace("Out of stock", "Add to Cart") # Replace all instances of 'Out of stock' with 'Add to Cart' to simulate a full stock drop.
        at_least_one_model_is_in_stock = "add to cart" in all_models_on_page.lower() 
        if at_least_one_model_is_in_stock:
            return stock_status_message(True)
        else:
            return stock_status_message(False)  

    #FALSE: We only care about a specific model.
    else:
        target_model_listing = all_models_on_page.split("00")[required_model_parsed] #Get the listing for your model only. We don't want the rest.
        
        if DEBUG_MODE_ON and random.random() < fake_in_stock_chance:
            print(f"\033[93mDEBUG INFO: Attempt {attempts}: For this run, we are simulating a real 'in stock' message on the webpage, for your chosen model, based on a low random chance. This is so you can see what it would do if your model was suddenly in stock...\033[0m")
            target_model_listing += "add to cart" #This is what the real listing would say if it were in stock.
        
        required_model_is_in_stock = "add to cart" in target_model_listing.lower() #If the word 'Add' is present for your model, we know it's in stock.
        if required_model_is_in_stock:
            return stock_status_message(True)
        else:
            return stock_status_message(False)

#Builds a status dictionary as to whether stock was found for the feedback loop.
def stock_status_message(stock_was_found):
    if stock_was_found:
        print(f"\033[92mStock was found.\033[0m")
        return {
            "status": True,
            "time_to_find": datetime.now() - start_time,
        }
    else:
        print(f"\033[93mNo stock as of {datetime.now()}, sorry! I will retry shortly...\033[0m")
        return {
            "status": False,
            "time_to_find": None,
        }