class User:
    def __init__(self, username, password, staff, account, balance):
        self.username = username
        self.password = password
        self.staff = staff
        self.account = account
        self.balance = balance

class Account:
    def __init__(self, id, pin):
        self.id = id
        self.pin = pin

###########################################################
####################  EDIT BELOW HERE  ####################
###########################################################
# General Configuration
DEBUG = True
THREADS_PER_PAGE = 8

# Database Configuration
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://bank:secret@database:3306/bank"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Slack Configuration
SLACK_ENABLED = False
SLACK_APIKEY = "xoxp-xx-xx-xx-xx"
SLACK_CHANNEL = "#bank"

# Bank Configuration
AMOUNT_PER_SERVICE_UP = 50
WHITE_TEAM_ACCOUNT = "1234567890"
TEAM_ACCOUNT_MAPPINGS = {
    # Format:
    # TeamNumber: Account("AccountNumber", "PIN")
    # AccountNumber must be 10 characters long
    # PIN can be a max of 10 characters
    1: Account("1000000001", "12345"),
    2: Account("2000000002", "12345"),
    3: Account("3000000003", "12345"),
    4: Account("4000000004", "12345"),
    5: Account("5000000005", "12345"),
    6: Account("6000000006", "12345"),
    7: Account("7000000007", "12345"),
    8: Account("8000000008", "12345"),
    9: Account("9000000009", "12345"),
    10: Account("1000000010", "12345"),
    11: Account("1100000011", "12345"),
    12: Account("1200000012", "12345"),
    13: Account("1300000013", "12345"),
    14: Account("1400000014", "12345"),
    15: Account("1500000015", "12345"),
    16: Account("1600000016", "12345"),
}

# Team Configuration
TEAM_INITIAL_MONEY = 80000.00

# Account Configuration
ACCOUNTS = [
    # Format:
        # User(username, password, is staff, account(account number, pin), balance)

    # Staff/White Team account
    User("staff", "secret", True, Account(WHITE_TEAM_ACCOUNT, "56789"), 1000000000.00),

    # Scoring account. Used to transfer money from. Note, this doesn't need a balance,
    # it's just here so the 'transaction' comes from an account, and not out of no
    # where
    User("scoring", "secret", True, Account("2000000000", "98765"), 0.0),

    # Now create the team accounts. You should basically copy and paste the following
    # line, except change the 'username' and 'password' field. Also replace the 'X' in
    # "TEAM_ACCOUNT_MAPPINGS[X]" with the team number.
    #
    # Example for team #3: User("team3", "team3spassword", False, TEAM_ACCOUNT_MAPPINGS[3], TEAM_INITIAL_MONEY) 
    #
    # User("teamx", "secret", False, TEAM_ACCOUNT_MAPPINGS[X], TEAM_INITIAL_MONEY)
    User("team1", "secret", False, TEAM_ACCOUNT_MAPPINGS[1], TEAM_INITIAL_MONEY),
    User("team2", "secret", False, TEAM_ACCOUNT_MAPPINGS[2], TEAM_INITIAL_MONEY),
    User("team3", "secret", False, TEAM_ACCOUNT_MAPPINGS[3], TEAM_INITIAL_MONEY),
    User("team4", "secret", False, TEAM_ACCOUNT_MAPPINGS[4], TEAM_INITIAL_MONEY),
    User("team5", "secret", False, TEAM_ACCOUNT_MAPPINGS[5], TEAM_INITIAL_MONEY),
    User("team6", "secret", False, TEAM_ACCOUNT_MAPPINGS[6], TEAM_INITIAL_MONEY),
    User("team7", "secret", False, TEAM_ACCOUNT_MAPPINGS[7], TEAM_INITIAL_MONEY),
    User("team8", "secret", False, TEAM_ACCOUNT_MAPPINGS[8], TEAM_INITIAL_MONEY),
    User("team9", "secret", False, TEAM_ACCOUNT_MAPPINGS[9], TEAM_INITIAL_MONEY),
    User("team10", "secret", False, TEAM_ACCOUNT_MAPPINGS[10], TEAM_INITIAL_MONEY),
    User("team11", "secret", False, TEAM_ACCOUNT_MAPPINGS[11], TEAM_INITIAL_MONEY),
    User("team12", "secret", False, TEAM_ACCOUNT_MAPPINGS[12], TEAM_INITIAL_MONEY),
    User("team13", "secret", False, TEAM_ACCOUNT_MAPPINGS[13], TEAM_INITIAL_MONEY),
    User("team14", "secret", False, TEAM_ACCOUNT_MAPPINGS[14], TEAM_INITIAL_MONEY),
    User("team15", "secret", False, TEAM_ACCOUNT_MAPPINGS[15], TEAM_INITIAL_MONEY),
    User("admin", "secret", False, TEAM_ACCOUNT_MAPPINGS[16], TEAM_INITIAL_MONEY),
]
