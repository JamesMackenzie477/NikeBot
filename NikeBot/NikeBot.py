import requests
import uuid
import Definitions
from PVACodes import PVACodes

# a requests based bot used to interact with nike
class NikeBot:

    # stores the bots headers
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}

    # creates a new bot linked with the given account
    def __init__(self, email, password):
        pass

    # creates a valid session
    def create_valid_session():
         # creates a new request session
        with requests.session() as session:
            # sets the session headers
            session.headers.update(headers)
            # gets the site cookies
            session.get("https://www.nike.com/")
            # validates the request status
            # validates the cookies
            if session.cookies['_abck'] and session.cookies['bm_sz']:
                # The Nike registration system works by checking a cookie known as _abck.
                # If the cookie has been validated by a certain bot check request (below) then nike will allow the request
                # if not, then nike will block said request. Below we are spoofing this bot check request.
                # constructs the request headers
                # sensor_headers
                # creates the sensor data string
                sensor_data = {"sensor_data": "7a74G7m23Vrp0o5c9993156.78-6,2,-36,-495,Mozilla/9.8 (Windows NT 0.9; Win16; x65; rv:90.7) Gecko/62913058 Firefox/89.3,uaend,01113,01495853,en-US,Gecko,7,2,5,0,917469,8920805,2562,2335,6135,1144,759,406,019,,cpen:3,i8:2,dm:1,cwen:9,non:6,opc:2,fc:6,sc:5,wrc:3,isc:854,vib:7,bat:9,x63:5,x28:3,6892,5.985977520547,415430645796,loc:-3,7,-00,-914,do_en,dm_en,t_dis-6,3,-95,-386,-6,7,-43,-744,1,9,7,2,120,272,1;9,7,2,5,2347,9369,7;3,5,0,6,4071,358,1;9,1,4,8,5398,142,0;6,2,1,9,9992,722,4;8,4,5,5,3947,7528,3;-8,4,-84,-526,-0,9,-09,-274,8,4,1329,385,474;2,0,3109,768,256;5,6,1910,844,024;2,8,8871,976,658;9,6,7229,333,977;2,3,1656,197,134;1,2,5788,955,707;9,6,6843,585,325;9,0,7447,898,502;4,1,2240,059,372;00,7,8653,223,901;27,3,7140,271,755;54,2,5347,884,913;94,0,3309,622,283;43,8,8054,862,685;62,3,1823,015,164;68,6,6093,491,351;22,1,2374,975,314;08,7,8785,146,059;25,3,7274,183,807;62,2,6572,709,078;02,0,4543,541,348;51,8,9188,795,738;70,3,2956,042,214;76,6,7125,436,405;91,3,81132,459,646,1394;-2,1,-46,-018,-3,3,-41,-260,-7,4,-23,-620,-1,8,-75,-689,-6,2,-36,-498,8,96;2,47;1,56655;-6,2,-36,-407,https://www.nike.com/us/en_us/s/register-3,3,-41,-264,1,669362,7,2,5,0,883046,74472,9,2168576125277,4,22750,3,34,4871,2,4,08249,610237,6,15C9D74A1CF0497B6C8CE1EF7831BFB166F0B5425D0E01642B9F952B4A01701A~-2~s+zIlI8eoIDG7/NATNrTBnNCC7AMcn3zgNQqpbXvJbI=~-2~-6,3379,207,-105826473,15607278-0,9,-09,-260,9,4-6,7,-43,-751,739,152,990,042,539,952,990,842,339,7,415,416,481,557,-2,1,-58,-251,7,2,5,0,7,2,1-0,9,-09,-86,-522690910;dis;;true;true;true;-88;true;45;14;true;false;2-0,3,-12,-75,9936-1,8,-75,-681,34409357-2,1,-46,-019,24474-6,7,-43,-763,;7;8;2"}
                # post the sensor data that will validate the _abck cookie for two requests
                sensor_response = session.post("www.nike.com/_bm/_data", data=sensor_data)
                # validates the response
                if sensor_response.json()['success']:
                    pass

    # changes the phone number associated with the account
    def change_number(self, number):
        pass

    # verifies the phone number linked to the account
    def verify_number(self, code):
        pass

    # logs into the given nike account
    @staticmethod
    def login(email, password):
        pass

    # registers a new user with nike
    @staticmethod
    def register(email, password, first_name="Undefined", last_name="Undefined", date_of_birth="1980-1-1", gender="M", country="US", locale="en_US"):
        # constructs the request headers
        register_headers = {
            "origin": "https://www.nike.com",
            "referer": "https://www.nike.com/us/en_us/s/register",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
            }
        # constructs the register query string
        register_query = {
            "appVersion": "422", 
            "experienceVersion": "356", 
            "uxid": "com.nike.commerce.nikedotcom.web",
            "locale": "en_US", 
            "backendEnvironment": "identity", 
            "browser": None, 
            "os": "Windows NT 6.1; Win64; x64", 
            "mobile": False, 
            "native": False, 
            "visit": "1", 
            "visitor": uuid.uuid4(), 
            "language": "en-US"
            }
        # constructs the register form data
        register_data = {
            "country": "US",
            "firstName": "dummy", 
            "gender": "M", 
            "lastName": "dummy", 
            "locale": "en_US", 
            "password": password, 
            "receiveEmail": False, 
            "registrationSiteId": "nikedotcom", 
            "welcomeEmailTemplate": "TSD_PROF_MS_WELC_T0_GENERIC_V1.0", 
            "emailAddress": email, 
            "dateOfBirth": "1980-1-1", 
            "username": email, 
            "account": {
                "email": email, 
                "passwordSettings": {
                    "password": password, 
                    "passwordConfirm": password
                    }
                }
            }
        # creates a new request session
        with requests.session() as session:
            # gets the site cookies
            session.get("https://unite.nike.com/access/users/v1", headers=register_headers)
            # posts the form data to nike
            register_response = session.post("https://unite.nike.com/access/users/v1", headers=register_headers, params=register_query, data=register_data)
            print(register_response.text)

if __name__ == '__main__':
    # registers a new nike account
    bot = NikeBot.register("HJHFdsfsd78@gmail.com", "FHHSfd89g89df")
    # changes the phone number associated with the account
    bot.change_number("+887874875")
